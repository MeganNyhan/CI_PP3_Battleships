# Hangman - Irish Counties Edition
 
[Veiw the project here]()
1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements](#user-requirements)
    3. [User Stories](#user-stories)
    3. [Flow Chart](#flow-chart)
4. [Technology](#technology)
    1. [Develpoment Languages Used](#develpoment-languages-used)
    2. [Frameworks and Tools used](#frameworks-and-tools-used)
5. [Features](#features)
6. [Testing](#testing)
    1. [Python Validation](#HTML-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals 
<ul>
    <li> The main goal of this project is to allow users to play a hangmna game beased on the counties of Ireland so they can test their knowledge.</li>
    <li>It also aims to create a game with a good user experience that offers real world feedback to the user.</li>
    <li> Finally the game is connect to a database (google spreadsheets) to allow the owner of the game to host a platform that will gather user information that could be use for the site's analytics.</li>
</ul>
<hr>

### User Experience:

### Target Audience 
<p> The target audience for this site is quite broad. Hangman is a game that is easily understanded by those who play it, but as the topic of the game is teh Irish counties, this restricts those that can play the game. Because of this the target audience of this game is limited to residents of Ireland and those that have access to a computer - which is still quite broad. </p>

### User Requirements
<p>As I have mentioned, we have a very large/ yet restricted target audience, and becasue of this the site has to be simple in design and very accessible, to those who have computers and have geographical knowledge of Ireland. Aiding this knowledge I have created a game with:</p>
<ul>
    <li> Straightforward navigation through intro and game play, including a possibility to replay the game.</li>
    <li>The game has real time feedback for users which allows them to understand if their guess is right, wrong or invalid.</li>
    <li> The option to personalise the game by entering your name. <li>
</ul>

### User Stories

### First time and Recurring Stories
<ol>
    <li>As a user, I want to be able to play the hangman game that will test my knowledge of the Irish counties.</li>
    <li>As a user, I want to be able to use the game as a spelling test to revise for Irish Geography quizes at school.</li>
    <li>As a user, I would like to be able to personalise the game and enter my name.</li>
    <li>As a user who not tech savy, I want to be able know heo to play the game with very little technical advancity.</li>
        <li>As a user who doesn't understand websites, I want to easily see if I have guessed the question wrong or right.
    </li>
    <li>As a user, i want real time feedback telling me if my guess was right or wrong.</li>
</ol>

### Site's Owner Stories
<ol>
    <li>As the owner of the site, I want my potential users to have a place where they can enter their name that will be linked to a database that will show me how long the user has stayed on the website.</li>
    <li>As the owner, I want to have a game that will create a positive experience for the players of the game.</li>
    <li>As the owner, I want a game that is accessible to anyone.</li>
    <li>As the owner, I want a game that, will offer the user real time feedback and will record if the user guessed the word right or got it wrong in a database.</li>
</ol>

### Flow Chart
<p> I used the flow chart to design a clear map of my site that would help me design the functionality of the site and the logic and guidence for user stories. I did this by using Lucid Chart</p>
<details><summary>Flow Chart</summary>
        <img src="docs/flow_chart/flow_chart.jpeg"></details>
<hr>

## Technology:

### Develpoment Languages Used

<ul>
<li> Python </li>
</ul>

###  Frameworks and Tools used
<ul>
<li> Git, GitHUb, and GitPod </li>
<li> Lucid Chart </li>
<li> Heroku </li>
</ul>

<hr>

## Features:
<p>This site has only one page, but the flow of the game is broken into a few parts.</p>

### Introduction

<ul>
    <li>The introduction of the game is split into two parts - A logo that displayes the name of the game and the input section for the user to input their name.</li>
    <li> This allows the user to easily see the name of the game they are playing and also input their name to the system so they can have a personalised experience of the site.</li>
    </ul>
 <p>User Stories covered : </p>
 <p>Site Owner's Stories covered: </p>
        <details><summary>Introduction</summary>
        <img src=""></details>

#### Game
<ul>
    <li>The welcome section of the site offers the users to play the hangman game.</li>
    <li> The user is prompted to input a single letter and if it is wrong the stickman is drawn.</li>
    <li> If the guess is right then the user is told that they have guessed correctly.</li>
    <li> If the user guesses all the letters right befire the stickman is hanged then the user is told they are the winner. If not the user is told that they lost because they ran out of guesses.</li>
    <li> When the user is finnished with the game, the game will ask if the user wants to replay the game.<li>
    </ul>
    <p> User Stories covered : </p>
    <p>Site Owner's Stories covered: </p>
        <details><summary>Game Display</summary>
        <img src="assets/images/welcome-section.png"></details>
<hr>

 ## Testing:

 ### Python Validation
<p> To Validate my Python I used the PEP8 Online Validation Service. All python code passed its Validation with no errors but a few warnings as shown below in the pictures.</p>

<details><summary>Python Validation</summary>
<img src="assets/images/home-val.png"></details>

### Testing User Stories

    1."As a user, I want to be able to view the services that I can avail of in my local community."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Services information grid| Navigate to the Services page, locate the services grid | Finds a service they are interested in and goes to the contact page using contact button |    Works as expected |
| Nav- Locate services and then contact button | On any page scroll up to the nav bar | Find the list of services | Works as expected |
<details><summary>User Testing 1</summary>
<img src="assets/images/user-story-1.jpg">
<img src="assets/images/user-story-2.jpg"></details>
<hr>

    2."As a user, I want to know where I can get a avail of printing in my area."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Services information grid| Navigate to the Services page, locate the services grid and read prinitng info box | Finds the printing box and goes to the contact page using contact button |   Works as expected |
| Nav- Locate services page, services list and then contact button | On any page scroll up to the nav bar | Find the list of services | Works as expected |
<details><summary>User Testing 2</summary>
<img src="assets/images/user-story-2.1.png">
<img src="assets/images/user-story-2.2.png"></details>
<hr>

    3."As a user with the view of visting the office, I want to know exactly where it is located."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Information and Google Maps| Navigate to the Contact page, locate the contact information and google maps box | Finds the location and travels to the office |   Works as expected |
|Google Maps in contact page and other contact information | On any page scroll up to the nav bar | Find the comapnies contact inforamtion and google maps box | Works as expected |
<details><summary>User Testing 3</summary>
<img src="assets/images/user-story-3.png"></details>
<hr>

    4."As a user who not tech savy, I want to be able to read, understand and navigate an easy and understandable website."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Navigation| Navigate to any pages in the site, and perform desired goal | Finds the information they wanted | Works as expected |
|Nav bar on top of each page | On any page scroll up to the nav bar | Find any information available to the user | Works as expected |
<details><summary>User Testing 4</summary>
<img src="assets/images/nav-bar.png">
<p> The nav bar is simple in design and offers 4 options</p></details>


<hr>

    5."As a user who doesn't understand websites, I want to easily find a phone number for the office so I can contact them."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Information | Navigate to the Contact page, locate the contact information and phone number or contact form | Finds the phone number and calls the office or uses the contact form to conact the office via email| Works as expected |
|Contact Information and contact form in contact page| On any page scroll up to the nav bar | Finds the companies contact inforamtion | Works as expected |
<details><summary>User Testing 5</summary>
<img src="assets/images/user-story-5.png"></details>

<hr>

    6."As a user who owns a local business, I want to contact them get a quote for the price of business cards."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Services Page, and Graphic Design box with contact button | Navigate to the Services page, locate the services information and the contact us button | Finds the phone number when redirected to the phone number and calls the office or uses the contact form to ask for a qoute |
|Services information grid, Contact Information and contact form in contact page| On any page scroll up to the nav bar | Finds the companies services information and contact inforamtion to ask for a qoute easily | Works as expected |
<details><summary>User Testing 6</summary>
<img src="assets/images/user-story-6.png"></details>

### Testing Site Owner's Stories

    1."As the owner of the site, I want my potential customers to have a place where they can view the services I offer."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Services information grid| Navigate to the Services page, locate the services grid | Finds a service they are interested in and goes to the contact page using contact button | Works as expected |
| Nav- Locate services and then contact button | On any page scroll up to the nav bar | Find the list of services | Works as expected |
<details><summary>User Testing 7</summary>
<img src="assets/images/user-story-7.png"></details>
<hr>

    2."As the owner, I want to have an online platform that can be a hub of information for the locals in the area."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home Page | Allows the owner to easily up date and change the information displayed on the site.| Works as expected |
| Home page is the landing page which users will land on firat | Update the website as needed | New information displayed | Works as expected |
<details><summary>User Testing 8</summary>
<img src="assets/images/home-user-story.png">
</details>
<hr>

    3."As the owner, I want a website that is accessible to anyone."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Simple style Navigation | Navigation allows users a restricted choice between possible pages they need information from (Restricted as it doesn't allow too many decisions) | Finds the information they need easily |   Works as expected |
|Nav bar at the top of page allows simple navigation throughput site, providing a good User Experience | On any page scroll up to the nav bar | Find the information they wanted seamlessly | Works as expected |
<details><summary>User Testing 9</summary>
<img src="assets/images/nav-bar.png">
<p> The Navigation bar is simple and easily used by anyone.</p></details>
<hr>

    4."As the owner, I want a site that will encourage my customers to use the services we have to offer."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Navigation, Services Page, and Services Grid| Navigate to the services page where you can view the services grid| Finds the information on the services they wanted | Works as expected |
|Nav bar on top of each page including a link to the services page | On any page scroll up to the nav bar and select the services tab | Find any information on services available to the user and offer the possibilitiy of contacting the centre for more information they need | Works as expected |
<details><summary>User Testing 10</summary>
<img src="assets/images/user-story-6.png">
</details>
<hr>

    5."As the owner, I want a site that will have the potential to be built upon in the future."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav bar with the option of expanding to hold more pages| Navigation bar is wide and I as a developer intend to add a blog section in the future among other pages | To have more options added to the nav bar without comprimising the readability| Works in progress |
<details><summary>User Testing 11</summary>
<img src="assets/images/nav-bar.png">
<p> The Navigation bar is simple and can easily be extended on any device..</p>
</details>
<hr>

    6."As the owner, I want the customers to easily locate the company."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Contat Page with a adress and google maps link | Navigate (using the nav bar) to the Contact Page and find at the top of the page an adress, and when scrolled down the user will find a map too | Find the location easily and travels to the office | Works as Expected|
|Contact page with address and map, also a phone number for back up incase someone doesn't understand the map| On any page scroll up to the nav bar and find the contact page | Finds the companies address and other location informtion | Works as expected |
<details><summary>User Testing 12</summary>
<img src="assets/images/user-story-3.png"></details>

## Bugs:

| **Bug** | **Fix** |
| ----------- | ----------- |
| Website Fonts don't work in Firefox and safari| Choose back-up font for other browsers |
| Website moves to the left on larger monitors | Add another media quiery for larger than laptop screens |
| The map moves to the left on mobile repository | change the width of the map in the html to fit desktop and tablet then mobile again and push footer down|
<hr>

## Deployment:
<p>In order to deploy my site I took the following steps using GitHub pages and Heroku:</p>

<ol>
<li> Clone or Fork my repository.</li>
<li> Create an account in the Heroku app, and within that create a new app.</li>
<li> Add a "Config Var" with a key 'PORT' and value '8000' in Heroku's settings.</li>
<li> Add buildbacks firstly for the python code, and then again for NodeJS.</li>
<li> Then link the app to the repository using the following steps:</li>
<ul>
<li>Manually - Click to deploy branch </li><br>
<p>or</p>
<li> Enable automatic deploys and follow the prompted instructions.</li>
</ul>
</ol>
<p> My link is: https://ci-pp3-hangman.herokuapp.com/ </p>
<hr>

<p> Forking the repository is done by the following steps:</p>
<ol>
<li>Within the GitHub repository, click "Fork" (a button) at the upper right hand corner.</li></ol>
<hr>
<p> Cloning the repository is done by the following steps:</p>
<ol>
<li>Within the GitHub repository, locate "Code" (a button) found at the top of the page.</li>
<li> Once selected, select which you prefere out of the following choise: HTTPS, SSH or GitHub CLI and press the copy URL to your clipboard.</li>
<li> Then open Git Bash.</li>
<li> Change the current directory to your desired location for the cloned directory.</li>
<li>Finally, type "git clone" and paste your URL.</li>
<li>Once you press enter your local clone is created.</li></ol>

## Credits:
### Source Code Used in Site

<p> Due to limitations in my knowledge I googled certain code that I wanted to use for the site, see code listed below:</p>
<ul>
<li>I also referenced the Love-Sandwhiches project to help with the grid for the Gallery Section, the social links from the footer and the contact form. It was not copied and pasted directly but it was used for help so I thought I would mention it.</li></ul>
<hr>

## Acknowledgements:
<p> I would like to take this oppurtuinity to thank and acknowlege the following people:
<ul>
<li> I would like to thank Mo Shami - my mentor - for his feedback and guidence whilst creating the project.</li>
<li> I would like to thank those on the code institute slack channel for help with any issues I had.</li>
</ul>
</p>