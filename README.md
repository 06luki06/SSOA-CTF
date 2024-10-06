# SSOA-CTF

## Members

- Brandl Martin
- Cimpo Aldin
- Riegler Lukas

## Theme

Building a CTF platform based on a Simpsons theme using Ctfd.

## Planned CTFS

- SSRF
- SSTI
- SQLI
- Privilege Escalation
- Insecure Object Reference

## Planned Path of Development

Overall, we plan to have one big CTF with multiple challenges.

Initial State: Springfield nuclear plant website login screen
website logs back "username is correct, password is incorrect" -> finding out user "homer" exists
Another part of the application is a section "Help homer waste time" -> with an input field for an URL
Putting a URL there makes the backend access it using Homer's basic auth. 

When you are in control of the URL, you can get Homer's basic auth.
The credentials then can be retrieved by decoding the basic auth header. Those can be used to login as Homer.

Onced logged in, you will get to an Employee Page. Here you can see a search field to find other colleagues.

The search returns the ID of the user. This ID can be used to access the user's profile page.
Using that, we can retrieve Mr. Burns' ID, which is the only user that has "isAdmin" set to true.

Next goal would be to find a way to get Mr. Burns' password. Either through SQL Injection or SSTI we may exploit the URL of the employee page to get the passwords of the users in MD5.

Decrypting Mr. Burns' password, we can login as him and see the CEO page.

The CEO page will have a button to "Launch the Nuke to Shelbyville". This button will only be visible if the user is Mr. Burns, even though it is deactivated for the moment.
To activate the button, a 8 digit code must be entered. To get this code, we will most likely implement some sort of Path Traversal.

The goal would be to activate the button and launch the nuke. This would be the final goal of the CTF. After pressing that, we may have Brian and Stewie Griffin appear and stop the nuke from launching. 

## Planned Responsibilities

Responsibilites will be assigned later on.