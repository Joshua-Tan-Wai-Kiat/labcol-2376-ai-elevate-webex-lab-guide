# Module 1: Setting up a Webex Calling org in the Control Hub [Approx 10 min]

> Use values assigned to your own lab pod. Do not copy example credentials or connectivity details into public documentation.

Webex Calling Licenses:

Webex Calling is available through the Cisco Collaboration Flex Plan. You must purchase an Enterprise Agreement (EA) plan or a Named User (NU) plan.

Webex Calling provides three license types:

Professional - These licenses provide a full feature set for your entire organization. This offer includes unified communications (Webex Calling), mobility (desktop and mobile clients with support for multiple devices), team collaboration in the Webex App, and the option to bundle meetings with up to 1000 participants per meeting.

Standard - is designed for users requiring standard calling capabilities with a single device. This license allows users to use either one hardware device (e.g., an IP Phone) or soft clients (mobile, desktop, or tablet) across platforms. While offering essential features like voicemail and hotdesking profiles, it does not support advanced functionalities such as virtual lines, Voice Queues agent configuration, or Microsoft Teams calling integration.

Workspaces (also known as Common Area) - Choose this option if you're looking for a basic dial tone with a limited set of calling features appropriate for areas such as break rooms, lobbies, and conference rooms.

In this lab, we will explore the Professional License option only.

## Module 1a: Bulk Import DID numbers, Assign Numbers to a Location and the user Charles Holland

In this module we will import random/fake phone (DID) numbers to the Control Hub, define the Main number for the location in Control Hub, and assign a number to the user Charles Holland. In a customer environment, when you have an existing PSTN provider and DID numbers, you can import all your DID numbers into Control Hub and assign them as the Main number and/or to any user for Webex Calling.

- Within Workstation 1, open the Chrome browser from the taskbar.

- For security reasons, Webex Control Hub signs out every 20 minutes (Idle timeout) by default. For this lab, let's make the idle time out longer so the Control Hub does not sign you out often during this lab. Go to MANAGEMENT > Organization Settings > Control Hub's idle timeout. Drop down the option for Control Hub idle timeout and select 12 hours or no timeout. Click Save.

- Go to SERVICES > PSTN & Routing. Click + Add Numbers.

- On the Add Numbers page, drop down the option for Location and choose dCloud. Since we are setting up this location for the first time, first we need to select the PSTN Connection for this location. Click Edit PSTN.

- You will be taken to Edit PSTN connection for dCloud (Location) and under the connection type choose Premises-based PSTN and click Next.

- On the following page, drop down the option for Routing Choice and choose None. Even though None option is being shown as selected, you still have to click the dropdown option and choose None again. Select the checkbox for the confirmation and click Next.

- On the following page click Add Numbers Now (bottom right corner). You will be taken back to Add Numbers page with the PSTN connection populated, click Next.

- Minimize the browser (and other applications), and on the desktop find a text file named DID_Numbers.txt. It will have some DID Numbers (Fake) prepopulated for you. Select all of them, copy and paste them into Enter phone numbers field on Control Hub as shown below. Some Numbers might be marked in Red; this is because that number is either already used or taken by someone else within Webex Calling. You can remove all those numbers marked in Red by clicking the cross button next to them. Click Save.

NOTE: You will not face this issue of numbers being taken in production as you own the numbers from your Telco (phone company) provider for your organization.

- Click Close on the following page and you will be taken to the Numbers page where you can see all the numbers you have just added.

- Now, let's assign one of these numbers to the dCloud Location as the main number. On the Control Hub, go to MANAGEMENT > Locations.

- Select the dCloud location. Go to the Calling tab, you will notice that under the Main Number field, there is a warning that reads You will not be able to make or receive calls until this number is added.

- Drop down the option for Main Number and choose any of the numbers you have imported above and click Save.

- As soon as you save, the warning will disappear, indicating now your location can make and receive calls.

## Module 1b: Assigning Calling Licenses to a user on Webex Control Hub

- Continuing on Workstation 1, Go back to the browser where you have logged in to Webex Control Hub before.

- Go to MANAGEMENT > Users.

- Select Charles Holland user from the list of users.

- On the user Summary page scroll down and click Edit Licenses

- On the next page click Edit Licenses (towards the bottom right) again.

- On the next page go to the Calling tab and check mark for both options Webex Calling and Professional and Click Save.

- On the next page, in the dropdown option for Location, select dCloud. Drop down Phone Number field and select one of the PSTN Numbers available. Select any number other than the number you have assigned as the Main Number (previous module). Populate the extension field with 6018 for the user. Click Save. Click Close.

NOTE: Note the PSTN Number you have assigned to Charles Holland in a text file. You will need this number later in the lab.

- You will be taken back to the user Summary page. Notice that under Licenses, now Webex Calling Professional has been added for the Calling service.

- This completes the Assigning Calling Licenses on the Webex Control Hub Module.
