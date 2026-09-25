# Module 2: Configuring a Local Gateway for Webex Calling [Approx 25 min]

> Use values assigned to your own lab pod. Do not copy example credentials or connectivity details into public documentation.

After you configure Webex Calling for your organization, you can configure a trunk to connect your Local Gateway (LGW) to Webex Calling. SIP TLS transport secures the trunk between the Local Gateway and the Webex cloud. The media between the Local Gateway and Webex Calling uses SRTP. You can also import your pre-owned DIDs into Control Hub.

There are two options to configure the Local Gateway for your Webex Calling trunk:

Registration-based trunk

Certificate-based trunk

In this lab, we will cover only Registration-based Trunk.

## Module 2a: Local Gateway Configuration

In this module there are sub modules that are CLI (Command Line Interface) based. These sub modules contain downloading the required Root certificate bundle for the Local Gateway (LGW), configuring voice class tenant, voice class SIP profiles, dial-peers and other required commands on the CLI. Due to time limitations, we have created a PowerShell script that adds the premises-based trunk in the Control Hub and generates the CUBE configuration for the Local Gateway. When the script is run, it will generate the entire required configuration for LGW and put it on Workstation 1 Desktop in a file called CL_LGW_ Config-Ready.txt. Once the configuration is generated, you can just copy and paste it in the putty session of the LGW and proceed to next steps.

Continuing on Workstation 1, minimize all applications and find a PowerShell script on Desktop named CL_Add_Trunk.ps1.

Right click on the file and choose Run with PowerShell.

It will open the PowerShell script window and execute the script. Once the script has been executed, the PowerShell window pane will close automatically. Then you will see a text file created on the Desktop called CL_LGW_Config-Ready.txt that contains the entire CUBE configuration required for the LGW. Double click and open the configuration file.

Copy all (use Ctrl + A) the contents of the file (CL_LGW_Config-Ready.txt). Go to the putty window and paste (Right click anywhere on the putty window).

Once all the configuration is entered on Putty, scroll up and make sure there are NO error messages for any of the commands.

NOTE: Ignore the error message about saving the configuration at the end.

- At this point, the LGW should initiate registration to Webex Calling and you should see the trunk in LGW and Webex Calling up/online. Wait for 2 to 3 minutes and then on the Putty window use the command below, you will see the registration status yes.

Configuration:

The status of the trunk can be seen in the output of this command; you can see here that the registration status is yes.

Once you see the trunk registration status is yes, you can continue to the next module.

## Module 2b: Verifying trunk status on Control Hub and assigning it to a route group/location:

Before we start to test the Local Gateway configuration, verify that the premises-based PSTN trunk shows online in Control Hub. Go back to the browser tab where you had Webex Control Hub Open.

Navigate to Services > PSTN & Routing > Gateway Configuration > Trunk. Select the trunk that was added in the above module. On the fly-out window under Details click Trunk Info/Manage.

Ensure the status in Control Hub shows Online as displayed above. If the status does not show online, it means that there is some configuration issue. You will need to verify your Voice Class Tenant and SIP profiles on the vCUBE platform.

Once you have verified that the trunk status is online, you can assign this trunk directly to a location or create a Route Group with that trunk and assign the Route Group to a location. Creating a Route Group with a trunk and assigning it to a location helps to have multiple trunks in a route group and in production environments, it avoids service disruptions.

Let's create a Route Group, Go to SERVICES > PSTN & Routing > Gateway Configuration > Route Group tab. Select Create Route Group.

It will bring up a new pop-up window to create a new Route Group. On the pop-up window populate the following and click Save.

Name: dCloud-RG

Trunks: Drop down the option and choose the only available trunk (dCloud-Auto)

It will create the new Route Group dCloud-RG with the trunk.

- Now we can assign this Route Group to the location. Click Locations (hyperlink) on the pop-up window. Select the dCloud location under available locations. On the dCloud location page, go to the PSTN tab. On the PSTN tab click Manage (next to PSTN Configuration > PSTN connection).

On the following page drop down the option for Routing Choice and choose the Route Group you defined. In this lab guide, it's named: dCloud-RG. Checkmark the option to confirm that you understand the impact of these changes. Also notice that as soon as you select the route group from the list, it displays the trunks in that Route Group. Click Next. Click Done (add numbers later) on the following page.

Now just to make sure the trunk is assigned to the location, go to SERVICES > PSTN & Routing > Gateway Configuration > Trunk

Under the Trunk tab for the dCloud-Auto (or your trunk name) In Use column should show Yes as shown below. Similarly, if you go to Route Group tab, it will show the dCloud-RG route group In Use.

This completes verifying the trunk status on Control Hub and assigning it to Route Group/Location.

Note: Test calls to and from PSTN will be done in the next sections, Modules 3 and 4.
