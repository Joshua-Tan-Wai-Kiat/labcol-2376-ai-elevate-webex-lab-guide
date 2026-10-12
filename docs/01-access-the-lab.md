> **Lab data notice:** Values in screenshots are examples from the source guide. Use the credentials, addresses, phone numbers, and session details assigned to your own pod.

# Accessing your Lab

Click on the Details from the dCloud eXPO page and use the Host, Username and Password to connect using Cisco Secure Client (formerly AnyConnect) to your dedicated dCloud session.

Record the Host, Username, Password, and Session ID displayed for your assigned session.

AnyConnect (Cisco Secure Client) Host: use the host shown in your session details.

AnyConnect (Cisco Secure Client) Username: use the username shown in your session details.

AnyConnect (Cisco Secure Client) Password: use the password shown in your session details.

Continue to next step after connecting to the pod via the Cisco Secure Client.

## Connect to Workstation 1 via Remote Desktop

Connect to the Remote desktop of Workstation 1. On your session topology click workstation 1 and click Remote Desktop to connect

<figure class="lab-figure">
  <img src="../assets/source-guide/image7.png" alt="Connect to the Remote desktop of Workstation 1. On your session topology click workstation 1 and click Remote Desktop to connect">
  <figcaption>Source guide screenshot 7. Use the values assigned to your own lab pod.</figcaption>
</figure>

Within Workstation 1’s Desktop, there will be a file named WEBEX_PASSWORD.txt as shown above. Launch the file to get the username and password for the Webex App and the Collaboration Control Hub for this lab.

## Login to Collaboration Control Hub from within Workstation 1

Lauch the Chrome browser from within workstation 1and go to https://admin.webex.com. Login using the credentials from the WEBEX_PASSWORD.txt file from the previous section. If you do not see the WEBEX_PASSWORD.txt file, follow the instructions below. Otherwise, begin Module 1 of this lab. All the lab tasks should be completed from within Workstation 1

Now you can proceed with the lab modules.

### Alternate instructions for accessing Collaboration Control hub

Before we can proceed to login to Collaboration Control Hub, we need the DNS name, username, password, and session ID. Within the session details page, select DNS Address and copy the top level FQDN as displayed below. In the example below:

DNS Address / FQDN of your Webex organization: use the top-level FQDN shown for your assigned pod.

Session ID: use the ID shown in your session details.

Control Hub Username: cholland@&lt;FQDN&gt;, using your assigned top-level FQDN.

Control Hub Password: dCloud + the last 4 digits of your Session ID + !

1) On your PC, open Chrome browser and navigate to https://admin.webex.com

2) Login as Charles Holland with email and password. Your password will be dCloudXXXX! where XXXX will be your last 4 digits of your Session ID found in your Session Details tab.

Once logged in, you should see this home page for Collaboration Control Hub:

Now you can proceed with the lab modules.
