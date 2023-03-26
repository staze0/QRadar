# DSM Custom

---

### Presentation :

You'll find custom device support module I've created.
Be careful with using this DSM in production environment because :

1. I'm and I'll not be responsible of any disruption or problem caused by one of my DSM
2. IBM do not support the following cases :

   1. Requests for assistance to write, modify, test, or tune custom log sources for administrators in the DSM Editor.
   2. QRadar Support does not validate or update regular expressions to override default event properties for custom log sources.
   3. Requests to create custom event properties in the DSM Editor.
   4. QRadar Support does not assist users with mapping events or creating custom QIDs for events in the DSM Editor.
   
      **source** : [QRadar: DSM Editor and custom log source cases and support policies](https://www.ibm.com/support/pages/qradar-dsm-editor-and-custom-log-source-cases-and-support-policies)
      
Nevertheless, if you encounter any issue, you can contact me with the detail and I'll be happy to help you and improve the DSM. You can also provide amelioration, I'll be glad too.

---

### HowTo :

+ Install the DSM, you need to have sufficient permission to do this action, if you can do one of the folloing steps contact your QRadar's administrator :

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

This DSM allows you to collect everything you want to collect from iptables. You'll will be able to monitor all the network flow that came in and out your server.

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

+ Article on the subject : [TBD](https://staze.fr/)

</p>
</details>
</li>

<li>
<details><summary>Custom Windows Firewall :white_check_mark:</summary>
<p>

#### Details :

This DSM allows you to collect everything you want to collect from Windows Firewall. You'll will be able to monitor all the network flow that came in and out your Windows server.

#### QIDs :

+ None

#### Properties :

+ `Destination IP`
+ `Destination Port`
+ `Source IP`
+ `Source Port`

#### Appendix :

+ Article on the subject : [TBD](https://staze.fr/)

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

This DSM allows you to parse and map events from OpenVPN server hosted on your Synology NAS. You'll be able to track connection to the VPN server and which private IP is assigned to which user.

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
</ul>

</p>
</details>
</li>
</ul>
