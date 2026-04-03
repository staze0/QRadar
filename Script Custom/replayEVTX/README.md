Installation of requirements:

```bash
pip install -r requirements.txt
```

Usage of the script:

```bash
python replayEVTX.py --help
usage: replayEVTX.py [-h] -i INPUT [-o {stdout,syslog}] [--server SERVER] [--port PORT] [--protocol {udp,tcp}] [--delay DELAY]
                     [--format {json,raw,xml,qradar,snare}] [--prefix PREFIX] [--hostname HOSTNAME] [--os_version OS_VERSION]

Replay logs from EVTX or plaintext EVTX files to send them locally or remotly to a specific server.

options:
  -h, --help            show this help message and exit
  -i, --input INPUT     Path to the input log file (EVTX or plaintext EVTX)
  -o, --output {stdout,syslog}
                        Output destination (default: stdout)
  --server SERVER       Syslog server address (default: 127.0.0.1)
  --port PORT           Syslog server port (default: 514)
  --protocol {udp,tcp}  Syslog protocol (default: UDP)
  --delay DELAY         Delay in seconds between logs (default: 0)
  --format {json,raw,xml,qradar,snare}
                        Log format (default: raw). Only 'raw' and 'qradar' developped, other format will not change log output.
  --prefix PREFIX       Static prefix to add to each log (default: empty)
  --hostname HOSTNAME   Hostname to include in Snare format (default: localhost)
  --os_version OS_VERSION
                        OS version to include in Snare format (default: <OS_version>)
```

EVTX samples you may want to use:
- https://github.com/Yamato-Security/hayabusa-sample-evtx
- https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack
- https://github.com/sbousseaden/evtx-attack-samples

More information about this script in my QRadar's blog: https://qradar.guru
