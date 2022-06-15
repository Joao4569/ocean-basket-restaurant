# Ocean Basket Restaurant Online Bookings

## Conception

My thinking was that given the requirements of the project, it would be very beneficial to formulate some kind of plan which would lay out the basic scope, logic and design of my project in order to have some kind of structure with which to work with in order to avoid missing any crucial steps during construction and make the whole construction process as efficient as possible.

I made use of the following resources in order to plan and visualise my project after reading the project requirements:
 - I made use of [Lucidchart](https://www.lucidchart.com/pages/) in order to visualise the scope and logic of my ideas and thought processes, as well to manage my project using Agile methodology and common practices, that were appropriate for this project and taught to me by Code Institute.
 - I made use of [Balsamiq](https://balsamiq.com/) in order to create a basic wireframe design for Luigi's webpages.


### Project Scope

After reading the requirements for the project and the User's goal for the idea that I chose, I started working on a flowchart in order to visualise my idea and the thought processes behind it. I came up with four main categories of requirements for the project, functionality required from the application, data needed for the required functionality, data tables which will store the data required and technologies that I would like to make use of for the project.

I did this in order to have some basic structure and goals laid out which I could use as a guideline for the construction of the project and as a form of checklist which I could use to keep track of my progression as I proceed with the constsruction of the application.

***Scope flowchart placeholder***

 - Functionality was divided into two categories. The first was for functionality that was needed in order to meet the clients requirements as per the User's goal, labeled as "Must have's" in red, and the second was for functionality that I thought may be useful for the business and also logical next steps after meeting the basic requirements of the project, labelled as "Could have's" in green.

***Functionality flowchart placeholder***

 - I divided Data into three categories which made up different entities that needed data attributed to them in order for the business logic behind the project to make sense to a client and owner, in a real world situation, given the requirements of the project and it's goal.

***Data flowchart placeholder***

 - My next logical step was to come up with some basic idea of how to organise and store important data in relational databases designed for different user's needs, namely clients and employees in a way that was logical as well as neccessary for the required functionality of the project. I decided two basic tables were needed, one for storing booking data and another for using some of that data in a usefull manner for various employee's needs.

***Data-table flowchart placeholder***

  - And next I had to decide on which technologies to use for the project in order to best suite it's requirements and application, I would have to use multiple languages and a MVC Framework. The languages would be HTML, CSS, Javascript and Python, and I chose Django as the Fullstack MVC framework and possibly also make use of Bootstrap for some UX and design features at a later stage.

***Technologies flowchart placeholder***


### Project Logic

Once I had a basic idea of what I wanted to create, I then proceeded to draw up a flowchart in order to visualise the logic behind the functionality required for the project. This I believe will be extremely helpfull throughout production of the applicaton bby giving myself a specific plan to follow and avoid any unnecessary detours during construction.

***Logic flowchart placeholder***


### Basic Wireframe Design

Once I had the basic scope and logic in place, I then proceeded to design a visual representation of what is needed for the basic functionality of the project from a user's point of view and how I would represent that.

***Wireframe placeholder***

## Project Setup

After completing the basic conception of my idea and designing some basic structure to it, I then proceeded to setting up my IDE for the project using the steps recommended by Code Institute, namely:
 - 1) Install Django and supported libraries
 - 2) Create new Django project and app
 - 3) Deploy project to Heroku --- 4)??
  - - 4) Set project to use Cloudinary and PostgreSQL --- 3)??

### Installing Django and supporting libraries

- 1) Install Django version 3.2 which is the Long Term Support version of Django and recommended by Code Institute for the use on our projects
- 2) Installed gunicorn as the server to run Django on Heroku
- 3) Installed supporting libraries, dj_database_url and psycopg2 in order to run PostgreSQL
- 4) Installed supporting libraries , in order to run cloudinary as storage for the project's images (dj3-cloudinary-storage)

### Create new Django project and app

- 5) Create requirements.txt file
- 6) Create new blank Django project named ocean_basket
- 7) Create new Django app called online_booking
- 8) Add online_booking app to settings.py file of ocean_basket project
- 9) Migrate changes to database after creating online_booking app
- 10) Test if app is working correctly

## Deployment on Heroku

- 1) Create the Heroku app
- 2) Attach the PostgreSQL database
- 3) Prepare the environment and setting.py files
- 4) Get the static and media files stored on Cloudinary

### Steps to create Heroku App

1. While in the Heroku dashboard after logging in, click on the button in the upper right hand section of the sceen and select to create a new app from the dropdown list.
2. Name the app and select your region of residence from the dropdown list.
3. Click on the "Create app" button.
4. Once you return to your dashboard, click in the resources tab.
5. In the field where you can search for Add-ons, type in postgres and select "Heroku Postgres" result from the search.
6. There will be an alert window diaplayed on your screen, select the appropriate plan from the dropdown list and click on the "Submit Order Form" button.
7. Now click on the settings tab.
8. Click on the "Reveal Config Vars" button.

### Setting up Config Vars

9. Copy the address next to the "DATABASE_URL", starting with postgres://....
10. Create an env.py file in the same directory as the manage.py file in order to store your secret environment variables
11. Import the Operating System library to the env.py file.
12. Set the OS environment variable to the copied address from Heroku i.e. os.environ["DATABASE_URL"] = "postgres://...."
13. Create and add "SECRET_KEY" variable to env.py file.
14. Return to Heroku and create the "SECRET_KEY" variable using your secret key from the env.py file and click the "Add" button.
15. Reference env.py file in the settings.py file by fist importing the Operating System library in the settings.py file just under the first import in the file.
16. Next import the dj_database_url library just under.
17. Now add a conditional statement that if os.path.isfile('env.py') is True, then "env" should be imported in order to prevent errors if the file is not found due to it being allocated to the ".gitignore" file as standard practice within the supplied IDE template provided by Code Institute.
18. In the settings.py file find the "SECRET_KEY" variable and set it with the value, os.environ.get('SECRET_KEY'), so that it can access our secret key as setup in the env.py file.

### Wiring up PostgreSQL Database

19. Scroll to DATABASES section of settings.py file and comment out the entire dictionary.
20. Create a new DATABASES dictionary with a key called "default" with the value of "dj_database_url.parse(os.environ.get('DATABASE_URL'))" in order to get the database url variable as setup in the env.py file so that I can use the Heroku database as the back end of the project.
21. Run the migration command in the IDE terminal window in order to migrate all migrations on the new database.
22. Once completed go back to the Heroku page and click once again on the "Resources" tab.
23. Now click on the Heroku Postgres link in order to check that the database is working as intended.



## Deployment Testing



## Features

### Existing Features

- __The Landing Page__

### Features Left to Implement

## Testing

- After creating the online_booking app, I tested it buy running the application and recieved visual confirmation that the application is working successfully from Django.
- Once the database was initially linked to the Heroku app, I followed the Heroku Postgres link, in the resources section, in order to check that the database was connected and working after my initial migrations were done.

- Found bug 
  - **Resolved** 
- Sourced most common media breakpoint widths on [www.freecodecamp.org](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/.) and made the site responsive down to minimum width of 320 pixels.
  - Mobile devices: 320px — 480px
  - iPads, Tablets: 481px — 768px
  - Small screens, laptops: 769px — 1024px
  - Desktops, large screens: 1025px — 1200px
  - Extra large screens, TV: 1201px and more
- Made use of Chrome developer tools for previewing and testing new designs for media queries as well as UX aspects.
- I have tested all buttons and links, they are all acting as intended.

### Validator Testing

#### Initial Validator Tests

#### Final Validator tests

### Unfixed Bugs

## Credits

### Content

 - All flowcharts used in this project were designed by making use of [Lucidchart](https://www.lucidchart.com/pages/)
 - All wireframes used in this project were designed by making use of [Balsamiq](https://balsamiq.com/)



### Media