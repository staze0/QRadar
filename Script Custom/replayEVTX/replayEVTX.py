import argparse
import time
import socket
import sys
import xml.etree.ElementTree as ET
import datetime
from evtx import PyEvtxParser

def send_syslog(log, server, port, protocol):
    """Send log to syslog server"""
    if protocol == 'udp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server, port))
    
    try:
        sock.sendto(log.encode(), (server, port))
    finally:
        sock.close()

"""
Function format_qradar_tsv can be delete/ignore
"""
def format_qradar_tsv(record_xml):
    """Convert XML record to QRadar TSV format"""
    root = ET.fromstring(record_xml)
    kv_pairs = []
    
    def extract_final_keys(element, prefix=""):
        for child in element:
            tag = child.tag.split('}')[-1]  # Remove namespace
            attrib_value = child.attrib.get('Name', None)
            if attrib_value and child.text and child.text.strip():
                kv_pairs.append(f"{attrib_value}={child.text.strip()}")
            elif not attrib_value and child.text and child.text.strip():
                kv_pairs.append(f"{tag}={child.text.strip()}")
            extract_final_keys(child, prefix + tag + ".")
    
    extract_final_keys(root)
    return '\t' + '\t'.join(kv_pairs) + '\t'

def get_log_type(keywords):
    """Determine log type based on Keywords value"""
    log_types = {
        "0x80000000000000": "Error",
        "0x80000000000002": "Warning",
        "0x8020000000000000": "Success Audit",
        "0x8010000000000000": "Failure Audit",
    }
    return log_types.get(keywords, "Information")  # Default to Information

def get_log_category(event_id):
    """Determine log category based on EventID"""
    event_categories = {
        range(4720, 4736): "User Account Management",
        (4740,): "Account Lockout",
        (4781,): "Account Name Change",
        (4624,): "Successful Logon",
        (4625,): "Failed Logon",
        (4648,): "Logon Attempt with Explicit Credentials",
        (4634,): "Logoff",
        (4672,): "Special Privilege Logon",
        (4673, 4674): "Privilege Escalation",
        (4732, 4733, 4756, 4757): "Group Membership Changes",
        (4719, 4739, 4902): "Policy Changes",
        (4656, 4663, 4660, 4661): "Object Access & File System",
        (4688, 4689): "Process Creation & Execution",
        (5156, 5157, 5158): "Network & Firewall",
        (4657,): "Registry Changes",
        (4697, 4698, 4699): "Windows Services & Scheduled Tasks",
        (1102, 1100): "System Integrity & Security Events",
        (4768, 4769, 4770, 4771, 4776): "Kerberos Authentication & Tickets",
        (4778, 4779): "Remote Access Events",
        (4726,): "User Account Deleted",
        (4728, 4735, 4741, 4765, 4766, 4772): "Malicious Activity Indicators",
    }

    for key, category in event_categories.items():
        if event_id in key:
            return category
    return "Other"  # Default category

def format_snare(record_xml, hostname, os_version):
    """Convert XML record to Snare log format"""
    root = ET.fromstring(record_xml)
    kv_pairs = []

    event_id = "Unknown"
    event_category = "Unknown"
    log_category = "<Log_Category>"
    log_result = "<Log_Result>"
    sid_type = "<SIDtype>"
    snare_counter = "839"
    hostname_overwrite = hostname
    provider = "<Log_Provider>"
    username = "<Log_Username>"
    username_configuration = 0
    timestamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    timestamp_header = datetime.datetime.now().strftime("%b %d %H:%M:%S")
    
    def extract_snare_data(element):
        nonlocal event_id, event_category, log_category, sid_type, provider, hostname_overwrite, username, log_result, username_configuration
        for child in element:
            tag = child.tag.split('}')[-1]  # Remove namespace
            if tag == "EventID" and child.text:
                event_id = child.text.strip()
            if tag == "Channel" and child.text:
                event_category = child.text.strip()
            if tag == "Keywords" and child.text:
                log_result = get_log_type(child.text.strip())
            if tag == "Computer" and child.text:
                if hostname == "logreplay_scripter":
                    hostname_overwrite = child.text.strip()
            if tag == "Provider":
                provider = child.attrib.get('Name')
            if tag == "Data" and child.attrib['Name'] == "TargetUserName" and child.text:
                username = child.text.strip()
                username_configuration = 1
            if tag == "Data" and child.attrib['Name'] == "SubjectUserName" and child.text and username_configuration == 0:
                username = child.text.strip()
            if tag == "Data" and "Name" in child.attrib and child.text:
                kv_pairs.append(f"{child.attrib['Name']}={child.text.strip()}")
            extract_snare_data(child)
    
    extract_snare_data(root)

    if event_id != "Unknown":
        log_category = get_log_category(int(event_id))

    return f"<133>{timestamp_header} {hostname_overwrite} MSWinEventLog\t1\t{event_category}\t{snare_counter}\t{timestamp}\t{event_id}\t{provider}\t{username}\t{sid_type}\t{log_result}\t{os_version}\t{log_category}\t" + " ".join(kv_pairs)

def process_evtx(file_path, output, server, port, protocol, delay, format_type, prefix, hostname, os_version):
    """Process EVTX logs with different formats"""

    parser = PyEvtxParser(file_path)

    for record in parser.records():
        if format_type == "qradar":
            log = format_snare(record['data'], hostname, os_version)
        elif format_type == "snare":
            log = format_snare(record['data'], hostname, os_version)
        else:
            log = record['data']
        
        send_log(prefix + log, output, server, port, protocol)
        if delay:
            time.sleep(delay)

"""
Never test, but can be used for plain text file
"""
def process_plain_text(file_path, output, server, port, protocol, delay, prefix):
    """Process plain text logs"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            log = prefix + line.strip().replace('\n', ' ')
            send_log(log, output, server, port, protocol)
            if delay:
                time.sleep(delay)

def send_log(log, output, server, port, protocol):
    """Send log to the appropriate output"""
    if output == 'stdout':
        print(log)
    else:
        send_syslog(log, server, port, protocol)

def main():
    parser = argparse.ArgumentParser(description="Replay logs from EVTX or plaintext EVTX files  to send them locally or remotly to a specific server.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input log file (EVTX or plaintext EVTX)")
    parser.add_argument("-o", "--output", choices=['stdout', 'syslog'], default='stdout', help="Output destination (default: stdout)")
    parser.add_argument("--server", default="127.0.0.1", help="Syslog server address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=514, help="Syslog server port (default: 514)")
    parser.add_argument("--protocol", choices=['udp', 'tcp'], default='udp', help="Syslog protocol (default: UDP)")
    parser.add_argument("--delay", type=float, default=0, help="Delay in seconds between logs (default: 0)")
    parser.add_argument("--format", choices=['json', 'raw', 'xml', 'qradar', 'snare'], default='raw', help="Log format (default: raw). Only 'raw' and 'qradar' developped, other format will not change log output.")
    parser.add_argument("--prefix", default='', help="Static prefix to add to each log (default: empty)")
    parser.add_argument("--hostname", default='logreplay_scripter', help="Hostname to include in Snare format (default: localhost)")
    parser.add_argument("--os_version", default='<OS_version>', help="OS version to include in Snare format (default: <OS_version>)")
    
    args = parser.parse_args()
    
    if args.input.lower().endswith(".evtx"):
        process_evtx(args.input, args.output, args.server, args.port, args.protocol, args.delay, args.format, args.prefix, args.hostname, args.os_version)
    else:
        process_plain_text(args.input, args.output, args.server, args.port, args.protocol, args.delay, args.prefix)

if __name__ == "__main__":
    main()

