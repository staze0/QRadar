# DSM Custom

---

### Presentation :

You'll find custom device support modules I've created.
Be careful with using this DSM in production environment because :

1. I am and I will not be responsible of any disruption or problem caused by one of my DSMs
2. IBM does not support the following :

   1. Requests for assistance to write, modify, test, or tune custom log sources for administrators in the DSM Editor.
   2. QRadar Support does not validate or update regular expressions to override default event properties for custom log sources.
   3. Requests to create custom event properties in the DSM Editor.
   4. QRadar Support does not assist users with mapping events or creating custom QIDs for events in the DSM Editor.
   
      **source** : [QRadar: DSM Editor and custom log source cases and support policies](https://www.ibm.com/support/pages/qradar-dsm-editor-and-custom-log-source-cases-and-support-policies)
      
Nevertheless, if you encounter any issue, you can contact me with the detail and I'll be happy to help you and improve the DSM. You can also provide amelioration, I'll be glad too.

---

### HowTo :

+ Install the DSM, you need to have sufficient permission to do this action, if you cannot do one of the following steps, contact your QRadar's administrator :

  1. Go to your QRadar extension management page (https://<QRADAR_FQDN>/console/do/qradar/extensionsManagementConsole).
  2. Click "Add"
  3. Click "Browse", then select the zip file throught the file explorer
  4. [Optionnal if you want to install the DSM later] Check the "Install immediately button
  5. Click "Add"
  6. [During the installation process] A summup with all changes will be display, you can review it then accept it

---

### DSM List :

<ul>
<li>
<details><summary>Custom Linux iptables :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to collect everything you want to collect from iptables. You will be able to monitor all the network flows that come from and go towards your server.

#### QIDs :

+ `Linux Firewall Accept`
+ `Linux Firewall Deny`

#### Properties :

+ `Destination IP`
+ `Destination Port`
+ `Event Category`
+ `Event ID`
+ `Log Source Time`
+ `Protocol`
+ `Source IP`
+ `Source Port`

#### Appendix :

+ Article on the subject : [Tips : Supervision du firewall Linux](https://staze.fr/tips-supervision-du-firewall-linux/)

</p>
</details>
</li>

<li>
<details><summary>Custom Windows Firewall :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to collect everything you want to collect from Windows Firewall. You will be able to monitor all the network flows that come from and go towards your Windows server.

#### QIDs :

+ None

#### Properties :

+ `Destination IP`
+ `Destination Port`
+ `Source IP`
+ `Source Port`

#### Appendix :

+ Article on the subject : [Tips : Supervision du firewall Windows](https://staze.fr/tips-supervision-du-firewall-windows/)

</p>
</details>
</li>

<li>
<details><summary>Synology :calendar:</summary>
<p>

<ul>
<li>
<details><summary>Custom Synology OpenVPN :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to parse and map events from OpenVPN server hosted on your Synology NAS. You will be able to track connections to the VPN server and which private IP is assigned to which user.

#### QIDs :

+ `OpenVPN Authentication Failure`
+ `OpenVPN Authentication Success`
+ `OpenVPN Debug Message`
+ `OpenVPN IP Attribution`
+ `OpenVPN Session Closed`
+ `OpenVPN Session Opened`
+ `[CUSTOM] Synology OpenVPN Message`

#### Properties :

+ `Event Category`
+ `Event ID`
+ `Post NAT Source IP`
+ `Source IP`
+ `Username`

#### Appendix :

+ Article on the subject : [TBD](https://staze.fr/)

</p>
</details>
</li>

<li>
<details><summary>Custom Synology Files :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to parse and map files events from your Synology NAS. It covers differents actions such as write/read and much more. Moreover it works for multiple kinds of files management (SMB/GUI...).

#### QIDs :

+ `File Access`
+ `File Creation`
+ `File Deletion`
+ `File Modification`
+ `File Upload`
+ `OpenVPN Session Opened`
+ `[CUSTOM] Synology Files Message`

#### Properties :

+ `Action`
+ `Destination IP`
+ `Event Category`
+ `Event ID`
+ `Filename`
+ `Source IP`
+ `Username`

#### Appendix :

+ Article on the subject : [TBD](https://staze.fr/)

</p>
</details>
</li>
   
<li>
More to come for Synology technology :smile:   
</li>
   
</ul>

</p>
</details>
</li>

<li>
<details><summary>Custom Teleport Bastion :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to collect logs of your Teleport Bastion. It is very helpful when you want to monitor who access to which ressource and what action is taken. Because, I don't have access to the Teleport document which describe every ID of every log, you will not have an exhaustive list of events but with time I will complete with unknow events.

#### QIDs :

+ `[Teleport] User Login Success`
+ `[Teleport] User Login Failure`
+ `[Teleport] Session Start`
+ `[Teleport] Session Closed`
+ `[Teleport] Session Closed`
+ `[Teleport] File Upload Success`
+ `[Teleport] Session Data`
+ `[Teleport] Certificate Creation Success`
+ `[Teleport] File Downloaded`
+ `[Teleport] File Uploaded`

#### Properties :

+ `Event Category`
+ `Event ID`
+ `Log Source Time`
+ `Pre NAT Source IP`
+ `Pre NAT Source Port`
+ `Source IP`
+ `Source Port`
+ `Teleport Cluster Name`
+ `Teleport Event Name`
+ `Teleport Filename`
+ `Teleport MFA Device Name`
+ `Teleport Server Hostname`
+ `Teleport Session Start`
+ `Teleport Session Stop`
+ `Teleport User Agent`
+ `Username`

#### Appendix :

+ Article on the subject : [TBD](https://staze.fr/)

</p>
</details>
</li>

</ul>
