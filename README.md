# SSOA-CTF

## Theme

Building a CTF platform based on a Simpsons theme using Ctfd.

## Planned CTFS

- SSRF
- IDOR
- SQLI
- BFLA
- RCE

## Planned Path of Development

Overall, we plan to have one big CTF with multiple challenges.

Initial State: Springfield nuclear plant website login screen

### SSRF

website logs back "username is correct, password is incorrect" -> finding out user "homer" exists
Another part of the application is a section "Help homer waste time" -> with an input field for an URL
Putting a URL there makes the backend access it using Homer's basic auth.

When you are in control of the URL, you can get Homer's basic auth.
The credentials then can be retrieved by decoding the basic auth header. Those can be used to login as Homer.

### IDOR

Onced logged in, you will get to an Employee Page. Here you can see a search field to find other colleagues.

The search returns the ID of the user. This ID can be used to access the user's profile page.
Using that, we can retrieve Mr. Burns' ID, which is the only user that has "isAdmin" set to true.

### SQLI

Next goal would be to find a way to get Mr. Burns' password. Using SQL Injection we may exploit the URL of the employee page to get the passwords of the users in MD5.

Decrypting Mr. Burns' password, we can login as him and see the CEO page.

### BFLA

The CEO page will have a button to "Launch the Nuke to Shelbyville". Next to it, there will be a `0/2 CEOs requested`. Mr. Burns can confirm this request, by pressing a confirmation button. Nevertheless, we still need another admin who requests this. So we will implement some kind of BFLA. Afther the second user approves the request, we can relogin as Mr. Burns again and click on the button for launching the nuke.

### RCE

On the nuke launching page, one last password has to be entered. Next to the input field, there is another one, where you can input any kind of input. The goal of this challenge is to retrieve a process.env variable that contains the password for launching the nuke.

The goal would be to activate the button and launch the nuke. This would be the final goal of the CTF. After pressing that, we may have Brian and Stewie Griffin appear and stop the nuke from launching.

## Planned Responsibilities

Responsibilites will be assigned later on.
