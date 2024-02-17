# Pulse Dashboard

---

### Presentation :

You'll find custom dashboard I've created.
Be careful with using this dashboard in production environment because:

1. I am and I will not be responsible of any disruption or problem caused by one of my dashboards
      
Nevertheless, if you encounter any issue, you can contact me with the detail and I'll be happy to help you and improve the dashboard. You can also provide amelioration, I'll be glad too.

---

### HowTo :

+ Install the Pulse application first, you need to have sufficient permission to do this action, if you cannot do one of the following steps, contact your QRadar's administrator :

  1. Go to your QRadar extension management page (https://<QRADAR_FQDN>/console/do/qradar/extensionsManagementConsole).
  2. Click "Add"
  3. Click "Browse", then select the zip file of the Pulse application ([https://exchange.xforce.ibmcloud.com/hub?q=pulse]) throught the file explorer
  4. Click "Add"
  5. [During the installation process] A summup with all changes will be display, you can review it then accept it
  6. After Pulse application installation process completed, refresh your QRadar and go on the Pulse tab
  7. Drill down the dashboard menu then click on "Import Existing" and "Select file"
  8. Select the JSON file from the dashboard you want to import, then click Open to proceed the installation

---

### Dashboard List :

<ul>
      
<li>
<details><summary>EPS Monitoring :white_check_mark:</summary>
<p>

#### Details :

This dashboard will allow you to monitor EPS and peaks of logs in your QRadar infrastructure.

#### [File](https://raw.githubusercontent.com/staze0/QRadar/main/Pulse%20Dashboard/EPS%20Monitoring.json)

#### Appendix :

+ Article on the subject (english version): [HowTo #4 - Monitor EPS](https://staze.fr/)
+ Article on the subject (french version): [HowTo #4 - Monitorer les EPS](https://staze.fr/)

</p>
</details>
</li>

<li>
<details><summary>Search Monitoring :white_check_mark:</summary>
<p>

#### Details :

This dashboard will allow you to monitor searches done on your QRadar infrastructure.

#### [File-TBD](https://github.com/staze0/QRadar/)

#### Appendix :

+ Article on the subject (english version): [HowTo #10 - Monitor searches](https://staze.fr/)
+ Article on the subject (french version): [HowTo #10 - Monitorer les recherches](https://staze.fr/)

</p>
</details>
</li>

</ul>
