# **Cocktails At Home**

**Milestone Project 3: Data Centric Development - Code Institute**

The Idea around building this site was to keep people entertained during lockdown at Home.  Basically to play around with Cocktails and follow ingredients on this site to create classics at home.  Fun for the adults


In Short:

- Fun activity for adults during lockdown and if they just need to have cocktail specs to make a classic at Home
- Users can log in and add cocktails to there profile


# **Demo**

A live Demo can be found [here](https://kevin1610433.github.io/MS2-TeenageMutantNinjaTurtlesGame/)

![Design](https://kevin1610433.github.io/MS2-TeenageMutantNinjaTurtlesGame/assets/images/fireshot.png)

# **UX**

This website has two navigatible pages.  The home page is just for simplicity with a 'Turtle Shell' background, consisting of an 'Enter' button to navigate to the next page in order to start the Game, an 'Instructions Modal' which pops up and gives you instructions on how the game works, then some social links that the user can follow and simply a copyright tag.  The second page is laid out with 'Buttons at the top of the page and then the cards laid out below.  This is a simple match the cards game with theme music involved.


## User Stories

- As a user I want it to test me each time I reset the game to see if i can improve or go quicker than before.
- As a user I particulary like the theme music and this takes me back to my childhood as I was a big fan of the Cartoon.
- As a user I wanted this to be a fun little game to play and get the family involved with it.
- As a user I wanted this game to be fun whilst travelling or if you simply have 5 minutes to kill wherever you are.
- I wanted the user to be able to browse this site on any device.

##  Bugs
-  Jinja showed me what line I went wrong on just to simply test if my site would load, spotted and changed


# **Features**

My website has two navigatable pages.  The first page is simply a home page, consisting of a full background image with centered a centered button, modal, Social links and a copyright tag.

- ENTER - This is a simple button on the index.html page which is linked to the main.html page which then opens another page, which essentially is the game 'Area'.
- INSTRUCTIONS/MODAL - This is a modal on the home page index.html.  This Modal when clicked pops up and give you instructions on how the game is meant to be played.
- SOCIAL LINKS/FOOTER - There are three links which the user can follow to take them to social links, they are: Facebook, Twitter and Github.  Then my name as copyright.
- START GAME - This Button once clicked will start the theme music and essentially start the Game.
- MUTE MUSIC - This Button once clicked will Pause the theme music and if you click start game it will resume where it was paused.
- HOME - This button once clicked will take you back to the Home page.
- RESTART - This Button will restart the game at any time once clicked.


## Features left to implement

I think if I need to add anything more to this site I would like to add a pop up modal once game is completed to congratulate the user and display the score and time with a restart function.  This will essentially come with more practice learning the language of Javascript.  I would also like to implement different levels of difficulty and maybe change the timer to a countdown to timer to really make the levels more difficult as the levels progress.  Unfortunately I couldnt get my move counter/timer to function properly, however with more research I feel I could introduce this once I initiate more practice with the Javascript Language.

# **Strategy**

I set out to make this a friendly, Colourful game with a theme tune to essentially relive my youth and have a bit of fun with it. The game is just some fun for the user weather they are young or old.

# **Scope**

The Scope for me was that I wanted to provide a fun Colourful user friendly environment to engage the user along with some theme music to keep them entertained.  For the adults it will take them back to the early 90's and will introduce kids into an all time favourite.

# **Structure**

The Structure of the game is laid out into two pages, the landing page consists of an Instruction Modal, with an Enter button which will you take you to the 'Game Page' and there is some social links on the landing page.  Once the user has been taken to the 'Game Page' there is a 'Start Game' button, 'Mute Music' button and a 'Home' button. 

# **Skeleton**

I used Balsamiq to create my wireframes - Third time I have used Balsamiq for my MS projects and I found it to be a very good tool, will continue to use this, I keep discovering more things to use with it.

![Wireframes](https://kevin1610433.github.io/MS2-TeenageMutantNinjaTurtlesGame/assets/images/wireframe/wireframe1.jpg)
![Wireframes](https://kevin1610433.github.io/MS2-TeenageMutantNinjaTurtlesGame/assets/images/wireframe/wireframe2.jpg)


# **Surface**

The Surface of my website was to obtain and eye catching feeling, I feel I obtained this by using lots of colour and interesting images of the Turtles.  I Used shutterstock for some of my images and the others I gained from the internet

# **Technologies Used**

- Html - Html was used to create the layout of the website
- CSS - CSS was used to syle my website
- Javascript - I used Javascript to flip my 'Game' cards around and incorporate the music function as long as the timer and move counter
- Balsamiq Wireframes - Balsamiq was used to create wireframes to get an idea of layout and changed slightly when I started coding
- [Bootstrap](https://getbootstrap.com/docs/4.5/components/modal/) - I used bootstrap for my modal and used container divs for my classes
- W3Schools - I found W3Schools extremelly helpful with this project and I used this audio to help with starting my theme music [W3Schools](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_audio_play) I then modified it a little.
- [Font Awesome](https://fontawesome.com/) I used font awesome for the icons
- [Google Fonts](https://fonts.google.com/specimen/Indie+Flower?sidebar.open=true&selection.family=Indie+Flower) - I used Google fonts for my fonts and I used "Indie-Flower" throughout the entire page as I think it works well with the site and fits the theme of the Turtles
- [W3Validator](https://validator.w3.org/nu/#textarea) - I used this to test my HTML and CSS
-  Materilize
-  Jquery


# **Testing**

I tested my site through Chrome and all seemed responsive.  I also tested my site through mobile, namely google pixel 3 and all seemed responsive also.  Tested through a Samsung Tablet also and again seemed responsive.  The only issue I would comment on this or say is that the images seem slightly blurred on smaller devices, the reponsivness works fine but pixelation of images is not.  This was tested through a number of smart phones and I encountered the same problems each and every time.  More research and studying is required to master this.

# **Deployment**

This site is deployed directly from GitHub, everytime this is updated it will automatically update the site. This site is deployed directly from GitHub itself.  This directory can be cloned to open on another IDE.  

[Click here for Website](https://kevin1610433.github.io/MS2-TeenageMutantNinjaTurtlesGame/)

[Click here for Repo](https://github.com/kevin1610433/MS2-TeenageMutantNinjaTurtlesGame)

# **Credits**

## Content

- I obtained code from free code camp for the Javascript game, which can be found here [here](https://medium.com/free-code-camp/vanilla-javascript-tutorial-build-a-memory-game-in-30-minutes-e542c4447eae), I also used some of the CSS styling from here and modified the code to suit my project.  I also obtained some code from a fellow student who built a similar game to me and I was intrigued how this student managed a simple yet such an effective game, I used some HTML, CSS, & Javascript from this student and again modified to suit my code.  You can find the link [here](https://github.com/karzuin/MS2)

## Media

- All media was obtained from shutterstock and google.  Media was an MP3 that my brother Derek Rogerson kindly gave to me.  All Media is for Educational purposes only and cannot be distributed.

## Acknowledgements

- I would like to acknowledge all the code that I obtained online from the above Acknowledgements, they have been an incredible help.
- I would also like to thank the Slack community and everyone at Code Institute, the support has been great.
- All images used from google is for Educational purposes only and they are not to be used to be dispersed.
- I would like to thank Karen Yeun a fellow student in Code Institute as this project helped me structure mine.  I would also like to thank my Wife Emma Rogerson who originally gave me the idea of doing a project on Teenage Mutant Ninja Turtles.
- Again I would like to say thanks to my Brother who helped me with the MP3 for the theme music as this has helped me incorporate this into my project.
