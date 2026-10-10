# Accessing your lab

Allow approximately 10 minutes for this section. You will connect to your assigned dCloud session, open Workstation 1, retrieve the pod-specific Webex credentials, and sign in to Collaboration Control Hub.

> The values shown in the lab environment are unique to your assigned session. Always use the host, username, password, session ID, and DNS name displayed for your own pod.

## 1. Find your session details

1. Open the dCloud eXPO page for this lab and locate your assigned session.
2. Select **Details**.
3. Record your **Session ID**. You may need it when identifying pod-specific resources.
4. Open the **AnyConnect** tab under the session details.
5. Copy the **Host**, **Username**, and **Password** shown for your session. Do not use values from an example screenshot or another participant's pod.

## 2. Connect with Cisco Secure Client

1. Open **Cisco Secure Client** on your computer.
2. Enter the AnyConnect host copied from the dCloud session details and select **Connect**.
3. When prompted, enter the assigned username and password.
4. Confirm that Cisco Secure Client reports an active connection before continuing.

<figure class="lab-figure">
  <img src="../assets/access/01-cisco-secure-client.png" alt="Cisco Secure Client prompting for the assigned dCloud username and password">
  <figcaption>Enter the pod-specific username and password from the AnyConnect session details.</figcaption>
</figure>

## 3. Connect to Workstation 1

1. Return to the dCloud session page and open the **Network** or topology view.
2. Locate **Workstation 1**. It can also appear as **wkst1**.
3. Select the **Remote Desktop** link for Workstation 1.
4. If the browser downloads an RDP file, open it and accept the connection prompt.
5. Use the Workstation 1 username and password displayed in your session details.
6. Confirm that the Windows desktop labelled **WKST1** is visible.

## 4. Find the Webex credentials

On the Workstation 1 desktop, locate **WEBEX_PASSWORD.txt** and open it. The file contains the pod-specific credentials used for the Webex App and Collaboration Control Hub.

<figure class="lab-figure">
  <img src="../assets/access/02-workstation-1-desktop.png" alt="Workstation 1 desktop with WEBEX_PASSWORD.txt highlighted in the lower-left corner">
  <figcaption>Workstation 1 desktop. The WEBEX_PASSWORD.txt file is highlighted in the lower-left corner.</figcaption>
</figure>

Keep the file open or record the following values in a private location:

- Control Hub administrator email address
- Webex password assigned to the pod

Do not copy these values into shared notes, screenshots, or the public lab guide.

## 5. Sign in to Collaboration Control Hub

1. From Workstation 1, open Chrome.
2. Go to [https://admin.webex.com](https://admin.webex.com).
3. Sign in with the Control Hub administrator email address and password from **WEBEX_PASSWORD.txt**.
4. If a privacy, cookie, or introductory prompt appears, complete it and continue.
5. Confirm that the Collaboration Control Hub home page loads for your assigned organization.

## If WEBEX_PASSWORD.txt is unavailable

Use the pod information shown in the dCloud session details rather than guessing credentials:

1. Open **Details > DNS Address** and identify the DNS name assigned to the pod.
2. Record the session ID from the same session details page.
3. Follow the credential convention provided by the lab proctor or dCloud session instructions.

If the credentials still cannot be determined, stop and ask the lab proctor. Do not use values displayed in screenshots from another session.

## Checkpoint

Before moving to Module 1, verify all of the following:

- Cisco Secure Client is connected to the assigned dCloud session.
- Workstation 1 is accessible through Remote Desktop.
- The pod-specific Control Hub credentials have been located.
- Collaboration Control Hub is open and shows the assigned organization.

You can now proceed to [Module 1: Set up the Webex Calling organization](02-webex-calling-org.md).
