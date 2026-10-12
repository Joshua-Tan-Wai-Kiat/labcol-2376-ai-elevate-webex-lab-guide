> **Lab data notice:** Values in screenshots are examples from the source guide. Use the credentials, addresses, phone numbers, and session details assigned to your own pod.

# Module 1: Setting up a Webex Calling org in the Control Hub

## Module 1a: Import DID numbers, Assign Numbers to a Location and the user Charles Holland

In this module we will import random/fake phone (DID) numbers to the Control Hub, define the Main number for the location in Control Hub, and assign a number to the user Charles Holland. In a customer environment, when you have an existing PSTN provider and DID numbers, you can import all your DID numbers into Control Hub and assign them as the Main number and/or to any user for Webex Calling.

1. Within Workstation 1, open the Chrome browser from the taskbar.
2. Go to the Webex Control Hub (https://admin.webex.com). Your pod’s Webex organization’s credentials are placed on the Desktop of Workstation 1 in a file called WEBEX_PASSWORD.txt. You will use the same credentials to login to the Control Hub and the Webex App for the user Charles Holland in this lab. Refer to the screenshots below.
3. Log in to the Webex Control Hub with your respective pod’s credentials from the file and not using the screenshot credentials shown above.
4. For security reasons, Webex Control Hub signs out every 20 minutes (Idle timeout) by default. For this lab, let’s make the idle time out longer so the Control Hub does not sign you out often during this lab. Go to MANAGEMENT > Organization Settings > Control Hub’s idle timeout. Drop down the option for Control Hub idle timeout and select 12 hours or no timeout. Click Save.
<figure class="lab-figure">
  <img src="../assets/source-guide/image12.png" alt="For security reasons, Webex Control Hub signs out every 20 minutes (Idle timeout) by default. For this lab, let’s make the idle time out longer so the Control Hub does not sign you">
  <figcaption>Source guide screenshot 12. Use the values assigned to your own lab pod.</figcaption>
</figure>

5. Go to SERVICES > PSTN & Routing. Click + Add Numbers.
<figure class="lab-figure">
  <img src="../assets/source-guide/image13.png" alt="Go to SERVICES &gt; PSTN &amp; Routing. Click + Add Numbers.">
  <figcaption>Source guide screenshot 13. Use the values assigned to your own lab pod.</figcaption>
</figure>

6. On the Add Numbers page, drop down the option for Location and choose dCloud. Since we are setting up this location for the first time, first we need to select the PSTN Connection for this location. Click Edit PSTN.
<figure class="lab-figure">
  <img src="../assets/source-guide/image14.png" alt="On the Add Numbers page, drop down the option for Location and choose dCloud. Since we are setting up this location for the first time, first we need to select the PSTN Connection ">
  <figcaption>Source guide screenshot 14. Use the values assigned to your own lab pod.</figcaption>
</figure>

7. You will be taken to Edit PSTN connection for dCloud (Location) and under the connection type choose Premises-based PSTN and click Next.
<figure class="lab-figure">
  <img src="../assets/source-guide/image15.png" alt="You will be taken to Edit PSTN connection for dCloud (Location) and under the connection type choose Premises-based PSTN and click Next.">
  <figcaption>Source guide screenshot 15. Use the values assigned to your own lab pod.</figcaption>
</figure>

8. On the following page, drop down the option for Routing Choice and choose None. Even though None option is being shown as selected, you still have to click the dropdown option and choose None again. Select the checkbox for the confirmation and click Next.
<figure class="lab-figure">
  <img src="../assets/source-guide/image16.png" alt="On the following page, drop down the option for Routing Choice and choose None. Even though None option is being shown as selected, you still have to click the dropdown option and ">
  <figcaption>Source guide screenshot 16. Use the values assigned to your own lab pod.</figcaption>
</figure>

9. On the following page click Add Numbers Now (bottom right corner). You will be taken back to Add Numbers page with the PSTN connection populated, click Next.
10. Minimize the browser (and other applications), and on the desktop find a text file named DID_Numbers.txt. It will have some DID Numbers (Fake) prepopulated for you. Select all of them, copy and paste them into Enter phone numbers field on Control Hub as shown below. Some Numbers might be marked in Red; this is because that number is either already used or taken by someone else within Webex Calling. You can remove all those numbers marked in Red by clicking the cross button next to them. Click Save.
NOTE: You will not face this issue of numbers being taken in production as you own the numbers from your Telco (phone company) provider for your organization.

11. Click Close on the following page and you will be taken to the Numbers page where you can see all the numbers you have just added.
12. Now, let’s assign one of these numbers to the dCloud Location as the main number. On the Control Hub, go to MANAGEMENT > Locations.
13. Select the dCloud location. Go to the Calling tab, you will notice that under the Main Number field, there is a warning that reads You will not be able to make or receive calls until this number is added.
14. Drop down the option for Main Number and choose any of the numbers you have imported above and click Save.
15. As soon as you save, the warning will disappear, indicating now your location can make and receive calls.
## Module 1b: Assigning Calling Licenses to a user on Webex Control Hub

1. Continuing on Workstation 1, Go back to the browser where you have logged in to Webex Control Hub before.
2. Go to MANAGEMENT > Users.
3. Select Charles Holland user from the list of users.
4. On the user Summary page scroll down and click Edit Licenses
5. On the next page click Edit Licenses (towards the bottom right) again.
6. On the next page go to the Calling tab and check mark for both options Webex Calling and Professional and Click Save.
7. On the next page, in the dropdown option for Location, select dCloud. Drop down Phone Number field and select one of the PSTN Numbers available. Select any number other than the number you have assigned as the Main Number (previous module). Populate the extension field with 6018 for the user. Click Save. Click Close.
NOTE: Note the PSTN Number you have assigned to Charles Holland in a text file. You will need this number later in the lab.

8. You will be taken back to the user Summary page. Notice that under Licenses, now Webex Calling Professional has been added for the Calling service.
9. This completes the Assigning Calling Licenses on the Webex Control Hub Module.
## Module 1c: Enable AI Assistant for Webex Calling

Before users can experience the capabilities of AI-driven collaboration, administrators must first lay the groundwork. This task focuses on activating and configuring the Cisco AI Assistant and its associated features within Collaboration Control Hub.

1. Go to ‘Management > Organization Settings > Cisco AI Assistant & AI features’. Click on Customize AI Assistant & AI features as shown below.
2. Ensure ALL the toggles are turned ON for the Calling AI features. Click ‘Save’
<figure class="lab-figure">
  <img src="../assets/source-guide/image26.png" alt="Ensure ALL the toggles are turned ON for the Calling AI features. Click ‘Save’">
  <figcaption>Source guide screenshot 26. Use the values assigned to your own lab pod.</figcaption>
</figure>
