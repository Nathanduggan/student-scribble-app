# Student Scribble

# Demo Link: <a href="https://student-scribble-app.herokuapp.com/">https://student-scribble-app.herokuapp.com/</a>

## The User's

When deciding upon the purpose of my App, I considered creating something that will make it easier for students to keep track of
homework, assignments and projects. The idea is that Students will be able to create accounts and log in each time. They will be able
to create a list of subjects and then select a subject to write a note on. For example, they could create a note that will remind them of what homework
they have to do for a particular subject, they will be able to select a date and whether or not the note is compete.
The student can edit notes as they go and delete them once complete.
They will be able to add Subjects and also remove Subjects they no longer need.
If the student/user runs into any trouble they can contact support and fill out a form detailing their issues or it can also be used as an
opportunity for them to ask questions.

The web application should fulfil the CRUD operations.

### Features
#### The Home Page:
The home page is where the student will see all the notes that they have created.
From here they can click on the note and a drop down will show them the message.
They will be able to edit the note or delete the note all from the home page. 

#### The About Page:
This page will explain what the students need to do in order to successfully use the App.
From creating an account to setting up subjects. 
 

#### The Support Page:
This page will offer support for the students. The student will have to fill out the form with their name and email and what issues
they are having. 

#### The Manage Subjects Page:
This page will list the subjects that the students have added. They will be able to edit subjects and also delete the subject.
At the bottom of the page will be an add subject button where the student will be able to add a new subject to the list. 


#### The Edit Note Page:
From the home page the student will be able to click on the edit button which will bring them to another page, On this page will appear
the original details of the note, such as the subject, the topic, the description and the date if selected.
Once the student changes the details and clicks edit note then the changes will be saved.

#### The Login Page:
This is where the student will have to enter their username and password to access their account.
If they do not have an account, they can register by clicking the link. 

#### The Register Page:
Here the student will be able to create an account. They will have to enter their name, username and create a password.

## Technologies Used:
 - <a href="https://getbootstrap.com" rel="nofollow">Bootstrap</a> for modern styling with responsive navigation, tables and cards 
 - Javascript for implementation of JSON files, pagination, button and search functionality.
 - <a href="https://jquery.com" rel="nofollow">Jquery</a> and Popper Js for Bootstrap functionality.
 - <a href="https://fonts.google.com" rel="nofollow">Google Fonts</a> for fast loading on Exo 2 font.
 - <a href="https://json.org/" rel="nofollow">JSON</a> for building a quasi database of records in JSON that can be loaded to individual pages.
 - Python(https://www.python.org) 
 - Flask(http://flask.pocoo.org) 
 - PyMongo 3.7.2(https://api.mongodb.com/python/current/) 

## Resources:
 - <a href="https://stackoverflow.com" rel="nofollow">Stackoverflow</a>
 - <a href="https://www.w3schools.com" rel="nofollow">W3 Schools</a>
 - Google

## Testing.

##### Navigation Bar:
   - Go to the Home page.
   - Across the navigation bar the user can click the add note and create a new note.
   - Back to the home page again and click the subjects which is also a drop down list, Which contains 'add subjects' And 'Manage subjects.'
     Both links will bring you to their own page. 
  -  The Logo and the Home button if clicked will both bring the user back to the home page.
  -  On the top left of the screen there is a menu option and if selected will display a side-navigation bar.
     In here the user will be able to navigate to all pages including, adding a note/ subject, about page, support page and also this is
     where the user most go in order to sign in. 
   
##### Social Links:
    - From the top of the page a user can like the Facebook page and they can also Share the page. 
    

##### My Notes:
    - From the home screen the user will see the my Notes in the 
      centre of the screen after they have created  it 
      If the user selects the note a drop down will display what message 
      they made, if any of course. 
      Above will display, the subject,
      the topic and the Date. 
      They will also be able to delete and edit the note by clicking on the respective buttons.
##### Support email form:
    - Go to Support page and fill out the form.
    - Type in your name. If nothing is entered an error will come after you 
      click the sign-up Button.
    - Type your email, again an error will pop up if nothing is entered
      or if the '@' Symbol isn't included.
    - When the user clicks in the email, name or questions box, the background 
      will turn grey in colour and once the
      user starts to type the text will be in white.
    - I have tested the Emailjs with multiple email address on all screen sizes
      and received every email to my email address: Nathan.duggan0@gmail.com
##### The Login Page:
    - For testing purposes username: Admin Password: Admin5
    - Here the user will have to enter their username and password that they 
      would have already created.
    - If the user enters wrong information then an error will appear telling
      the user that their credentials are incorrect. 
    - If they have not yet registered, they can do so by clicking on the link 
      below the password box. 
##### Register Page:
    - Here the user will have to enter their name, create a username and create 
      a password.
    - They will have to create a username that doesn't already exist or less 
      they will get an error. 
    - Once they have successfully created an account, they will be redirected 
      to the Login screen page so that they can Login. 

## How it looks on different screen sizes and browsers:
   - Mobile: The pages fit in nicely, '375 X 667'. The Navigation bar is changed to a Hamburger drop down.
   - Everything else fits in a 'Col-xs-12' Grid including the Footer 
   - Tested ‘Sign up form’, Links in footer and ‘Read more’ button and all Works.
   - Tablet: Again, fits nicely '768 X 1024'. The Navigation stays the same as Desktop screen.
   - I have tested all screens on multiple Browsers, including,
     Google Chrome, Safari, Firefox and Internet Explorer.
## Deployment: 
    - I have deployed this project on both Github and Heroku
    - I first ran a git init and started to track my files/images and committed them and then 
      pushed them up to Github, were they all open and load with no issues. 
    - I then logged into my github profile page and clicked on my project's name.
    - Clicked on settings, scrolled down to Github Pages,
    - Under source, Selected master branch. 
    - Deployment Github Link: https://nathanduggan.github.io/student-scribble-app/
    - Heroku Deployment: Python package runs the http server for the app, the
      Procfile gives Heroku the information to run the app and requirements.txt is a file that
      contains all the Python packages required to run the app.
    - MongoDB was chosen to host the dataset on the server.
    - Heroku Link: https://student-scribble-app.herokuapp.com/
    - After setting up the Heroku account I simple connect Heroku with Github
      and pushed the code to deployed the Branch.



## Contents:
   - The Images on each paged are from Google Images.
   - The Navigation bar is from Materialise, Along with the drop down menu for the Notes.
   - The Side Bar is from Materialise, The icons from Google Icons.
 

## Acknowledgment: 
     I received inspiration for this project from my partner Natasha Thompson (Tash). Tash is a  
     Teacher in Bray and was always complaining that the children are never organised with 
     Homework/Notes Etc
     I would also like to thank my mentor Guido . His support throughout has been
     of great assistance. 
     Lastly, I would like to acknowledge my Dad who encouraged me to start this course in the 
     pursuit of bettering my career prospects.
