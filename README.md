# Hangman - Irish Counties Edition
 
[Veiw the project here](https://love-battleship.herokuapp.com/)
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
<p> The target audience for this site is quite broad. The centre itself offers printing, graphic design, bookeeping, social prescribing, room rental, and support for the over 65's. On the daily, the centre would have members of the public from varied backgrounds, technical abilities and age groups. </p>

### User Requirements
<p>As I have mentioned, we have a very large/ varied target audience, and becasue of this the site has to be simple in design and very accessible. They way I have tackled this are as follows:</p>
<ul>
    <li>Simple navigation that is non-ambiguous</li>
    <li>Have skimmable text in paragraphs so that users can easily and quickly find what they are looking for.</li>
    <li>Simple presentation of content on the page that make logical sense. </li>
    <li>A functional responsive wesite that allow the user to view the site regardless of screen size. </li>
    <li>A straightforward and professional form that allows users to easily contact the business.</li>
</ul>

### User Stories

### First time and Recurring Stories
<ol>
    <li>As a user, I want to be able to view the services that I can avail of in my local community.</li>
    <li>As a user, I want to know where I can get a avail of printing in my area.</li>
    <li>As a user with the view of visting the office, I want to know exactly where it is located.</li>
    <li>As a user who not tech savy, I want to be able to read, understand and navigate an easy and understandable website.</li>
        <li>As a user who doesn't understand websites, I want to easily find a phone number for the office so I can contact them.
    </li>
    <li>As a user who owns a local business, I want to contact them get a quote for the price of business cards.</li>
</ol>

### Site's Owner Stories
<ol>
    <li>As the owner of the site, I want my potential customers to have a place where they can view the services I offer. </li>
    <li>As the owner, I want to have an online platform that can be a hub of information for the locals in the area.</li>
    <li>As the owner, I want a website that is accessible to anyone.</li>
    <li>As the owner, I want a site that will encourage my customers to use the services we have to offer.</li>
    <li> As the owner, I want a site that will have the potential to be built upon in the future.</li>
    <li> As the owner, I want the customers to easily locate the company.</li>
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
</ul>

<hr>

## Features:
<p>This site has four pages with a total of nine features.</p>

### Home Page

#### Navigation Bar

<ul>
    <li>The navigation bar is featured on all four of the pages that make up the website. The navigation bar includes links to the Home Page, the Services Page, the Gallery Page and the Contact Page, and also the logo that re-directs you to the home page. The navigation bar is identical on each page to allow for easy navigation for each of the users. The design of the navigation bar is simple to limit ambiguity with the user. </li>
    <li> The main purpose of the navigation bar in the site is to allow the user easy travel through the site without the need of a previous or back button. </li>
    <li> The navigation will also be responsive across all devices, which will also serve to the accessibilty of the site do a myriad of users.</li>
    <li>The page that the users is on currently is underlined.</li>
    </ul>
 <p> User Stories covered : 4</p>
 <p>Site Owner's Stories covered: 3, 5 </p>
        <details><summary>Navigation</summary>
        <img src="assets/images/nav-bar.png"></details>

#### Welcome Section
<ul>
    <li>The welcome section of the site offers a quick introduction to the company.</li>
    <li> It also include an image of the building so the office is easily identifiable and esay to locate.</li>
    </ul>
    <p> User Stories covered : 4</p>
    <p>Site Owner's Stories covered: 2</p>
        <details><summary>Welcome Section</summary>
        <img src="assets/images/welcome-section.png"></details>

#### Meet the Team Section
<ul>
     <li>
     Also featured on the main page is a meet the team section which shows the user who they can expect to see when they visit the office.</li>
     <li> The meet the team section also goes into detail of what each person work as and what they can help you with.
     </li>
     <li> The main purpose of this section is to offer a freinsly introduction to the people you can expect to see in the office if you decide to go in.</li></ul>
     <p> User Stories covered : 4, 6</p>
     <p>Site Owner's Stories covered: 5, 5 </p>
        <details><summary>Meet the Team</summary>
        <img src="assets/images/meet-the-team-feature.png"></details>

#### Footer
<ul>
     <li> The footer allows the user to contact and view the social media pages that the organisation have.</li>
     <li> The social media links comprise of the respective social network icons for easy accessibility.</li>
     <li> The reason the design is so simple is that I didn't want it to be too cluttered with information. I felt less is more.</li></ul>
     <p> User Stories covered : 4, 6,</p>
     <p> Site Owner's Stories covered: 2, 3</p>
        <details><summary>Footer</summary>
        <img src="assets/images/new-footer.png"></details>

### Services Page
#### Services Grid and Contact us for more Button
<ul>
    <li> The services page is very plane. It features a grid style list of services that the resource center provides with a button to redirect the user to the contact page in a new tab.</li>
    <li> The purpose of adding the contact button is so that users will be redired to the contact page to encourage them to contact the company about the services they are interested in. This covers a site owner story too.</li>
    </ul>
    <p> User Stories covered : 1, 2, 4, 6</p>
    <p>Site Owner's Stories covered: 1, 2, 3, 4</p> 
        <details><summary>Services grid and Contact Button</summary>
        <img src="assets/images/services-grid.png"></details>

### Gallery Page

#### Gallery grid
<ul>
    <li>The gallery page features a grid of photos taken of the local community.</li>
    <li> The main purpose of the gallery is to encourage users to get active in the community and be aware of the events that are taking place.</li></ul>
    <p> User Stories covered : 3, 4</p>
    <p>Site Owner's Stories covered: 2, 4</p>
        <details><summary>Gallery Grid</summary>
        <img src="assets/images/gallery-features.png"></details>

### Contact Page

#### Google Maps Feature and Contact Form
<ul>
    <li>The contact page offers the user a chance to view the location of the office in the Milford Area on Google Maps. </li>
    <li> The contact form offers the users to message the office to ask about a certain service, or inquire about general queries easily and directly.</li>
    <li> Another purpose of th contact page and it's elements is to encourage the user to contact the office to inquire about the services offered.</li></ul>
    <p> User Stories covered :2, 3, 5, 6</p>
    <p>Site Owner's Stories covered: 2, 4, 6</p> 
        <details><summary>Contact: Google Maps and form</summary>
        <img src="assets/images/google-maps&-form.png"></details>
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
<li>Clone or Fork my repository.</li>
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
<p> My link is: https://megannyhan.github.io/CI_PP1_MDRC/ </p>
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
<li> I would like to thank my manager who helped me with Site Owner's stories to help guide the creation and purpose of the site.</li>
<li> I also want to say that I did intend on making a error 404 page but ran out of time.</li>
</ul>
</p>