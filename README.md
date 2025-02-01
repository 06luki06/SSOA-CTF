# SSOA-CTF

## Theme

Building a CTF platform based on a Simpsons theme using Ctfd as the ctf-platform.

## Planned CTFS

- SSRF
- IDOR
- SQLI
- BOPLA
- Brute-Force / BFLA

## Planned Path of Development

Overall, we plan to have one big CTF with multiple challenges.

Initial State: Springfield nuclear plant website login screen and introduction.

### SSRF - Server Side Request Forgery

website logs back "username is correct, password is incorrect" -> finding out user "hSimpson" exists
Another part of the application is a section "Help homer waste time" -> with an input field for an URL
Putting a URL there makes the backend access it using Homer's basic auth.

When you are in control of the URL, you can get Homer's basic auth.
The credentials then can be retrieved by decoding the basic auth header. Those can be used to login as Homer.

### IDOR - Insecure Direct Object Reference

Onced logged in, you will get to an Employee Page. Here you can see a search field to find other colleagues.

The search returns the ID of the user. This ID can be used to access the user's profile page.
Using that, we can retrieve Mr. Burns' ID, which is the only user that has "isAdmin" set to true. The hint is checking the URL.

### SQLI - SQL Injection

Next goal would be to find a way to get Mr. Burns' password. Using SQL Injection we may exploit the URL of the employee page to get the passwords of the users in MD5. The `comments/{id}` route is vulnerable.

Decrypting Mr. Burns' md5 password, we can login as him and see the CEO page.

### BOPLA - Broken Object Property Level Authorization

The CEO page will have a button to "Launch the Nuke to Shelbyville". Next to it, there will be somethling like `0/2 CEOs requested` (or similar). Mr. Burns can confirm this request, by pressing a confirmation button. Nevertheless, we still need another admin who requests this. So we will implement some kind of BOPLA. Afther the second user approves the request, we can click on the button for launching the nuke.

### Brute-Force / BFLA - Broken Function Level Authorization

On the nuke launching page, one last pin has to be entered. The correct pin code can be achived using brute force. Nevertheless, there is som kind of rate limiting - luckily Mr. Burns has the ability to create new users. And the route for entering the pin only requires an authenticated user (BFLA).

The goal would be to activate the button and launch the nuke. This would be the final goal of the CTF. After pressing that, you will get some kind of surprise.

## Planned Responsibilities

We are a team. So we get judged together!
