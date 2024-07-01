# Meal Share Backend drf.

This is my Back-End Django REST Framework for my PP5, Meal Share. 

Visit the deployed Back-End here: [Meal Share Back-End](https://df-api-project5-f27c63867984.herokuapp.com/)
    - This would mainly be to log in as admin to the site.

## CONTENTS

* [User Experience](#user-experience-ux)
  * [Planning Process](#planning-process)
  * [Design](#design)
* [Features](#features)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Websites & Programs](#websites-programs)
* [Deployment](#deployment)
* [Testing](#testing)
   * [Manual Testing](#manual-testing)
   * [Validator Test](#validator-test)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgments](#acknowledgments)

## User Experience (UX)


## Planning Process


## Design

The base layout/design is used from the walkthrough project 'I Think Therefor I Blog' and Crispy Forms. I did customize most aspects of Character Share to better suit my wants for the site.

## Features

### Admin Panel
A superuser can log into the admin panel by going to the main page and appending a /admin and then logging in.
Here the admin can edit, delete, and add everthing. 

<details><summary><b>Admin Panel</b></summary>

![Adminpanel](static/images/readme/adminpanel.png)

</details><br/>

## Technologies 

### Languages 

* Python -Provides the functionality for the Character Share.
* HTML5 - Provides the content and structure for the Character Share.
* CSS - Provides the styling for the Character Share.
* JavaScript - Provides interactive elements of the Character Share.
* React - Frontend

###  Websites & Programs 
* [Bootstrap](https://getbootstrap.com/) - Build fas, responsive sites with this frontend toolkit.
* [Django](https://www.djangoproject.com/) - Framework for building apps quickly and with less code.
* [Balsamiq](https://balsamiq.com/) - For wireframes.
* [Chatgpt](https://chat.openai.com/) - Used to help identify problems in code and possible way to solve them.
* [Github](https://github.com/) - Created repository and stored files here after commits. Users Stories and project board.
* [Heroku](https://heroku.com/) - For deploying Character Share.
* [Microsoft Visual Studio](https://visualstudio.microsoft.com/) - Wrote code and did commits to Github from here.
* [W3 School](https://www.w3schools.com/) Read and used as a guide for some code.
* [DjangoREST framework](https://www.django-rest-framework.org/)Guide and reference for code.

## Deployment 
Here I will describe the deployment procedure for the Back-End part of my project.

1. Creating a Code Institue database.
    * By entering my email to the CI database creator, a database was created for me.  [CI databasemaker](https://dbs.ci-dbs.net/)
    * Following the link sent to my email, shows the created database.
    * Most important part you will need is the Database URL, click the info button to copy that for later.
2. Setting up Heroku App.
    * Log into your Heroku account and go to the Dashboard.
    * Click 'New' --- 'Create new app'
    * Choose a unique name for your app and your region, then click 'Create App'.
    * Now go to the Setting tab of app. and click on the 'Reveal Cofig Vars'.
    * In the Key field enter 'DATABASE_URL' and for the Value paste your database URl without the quotes.
    * Click the 'Add' button to add it to the Config Vars.
3. Prepare your project in your IDE.
    * In the terminal in your project file, install dj_database_url and psycopg2 by typing: "pip3 install dj_database_url==0.5.0 psycopg2".
    * In the setting.py file, import dj_database_url underneath the import for os.
    * Update the Databases section to look like the following:  [Databases](readme_assets/images/dburl.png)
    * Create the env.py file if you do not have it. Now add a new environment variable with a key set to DATABASE_URL and the value as your database URL from earlier. code should be like so: " os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"
    * Migrate your database with: "python manage.py makemigrations" then: "python manage.py migrate".
    * To check that your database is connected and working, create a superuser: "python manage.py createsuperuser" --- To get to the admin panel append a "/admin" to the end of the url when running server.
4. Preparing code to be able to deploy on Heroku.
    * In order to be able to deploy to Heroku, we need several packages and files.
    * In the terminal install gunicorn: "pip3 install gunicorn django-cors-headers", and update your requirement.txt afterward: "pip freeze --local > requirements.txt".
    * Create a Procfile(which is required by Heroku) and insert the following: first line - "release: python manage.py makemigrations && python manage.py migrate" second line - "web: gunicorn drf_api.wsgi".
    * In settings.py update the ALLOWED_HOSTS to include your Heroku app's URl like so: " ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']".
    * In settings.py add 'corsheaders' to INSTALLED_APPS and then add 'corsheaders.middleware.CorsMiddleware' to the top of the MIDDLEWARE.
    * In settings.py underneath MIDDLEWARE, add the following for network requests: [CORS_ALLOWED](readme_assets/images/cors.png) Replace URLs with your own URLs.
    * Since front end and my Back-End are separate, you need add code to make cookies work. Add the following: [JWT](readme_assets/images/jwt.png)
    * In settings.py, replace the value of SECRET_KEY with: "= os.getenv('SECRET_KEY').
    * In your env.py create a new environment vairable for SECRET_KEY: 'os.environ.setdefault("SECRET_KEY", "CreateyourownsecretkeyhereCanbeANYTHING")'
    * In settings.py set debug to be True only if the Dev env. varibable exists. This means it is True in development, and False in production if set like this: "DEBUG = 'DEV' in os.environ" and in env.py "os.environ['DEV'] = '1'".
    * Update requirements.txt again and then add, commit and push to GitHub.
5. Deploying on Heroku
    * Go to you app on Heroku and then the Settings tab, open up the Config Vars. Add to it your SECRET_KEY, CLOUDINARY_URL, and DISABLE_COLLECTSTATIC if it is not there yet. For future, when you connect your Back-End to your Front-End, you can add CLIENT_ORIGIN. So the Config Vars should look like this: [Config Vars](readme_assets/images/configs.png).
    * The SECRET_KEY value is the one you created in your env.py file.
    * CLOUDINARY_URL value is the one you should have in your env.py after you installed Cloudinary to your project.
    * The CLIENT_ORIGIN value will the the url for the deployed front end.
    * In Heroku, go the the Deploy tab and under Deployement Method, click to connect to your Github account.
    * Search for you Back-End repo and then 'Connect'
    * Click the 'Manual Deploy' to deploy manually after every update on GitHub, or you can activate the 'Automatic Deployement' which will try to deploy after every new push to GitHub.
    * Now that it is deployed, you can click on the 'Open App' button in the top right hand off the screen in Heroku.



#### How to Fork in Github

If you want to fork this repository in Github:

1. Go to the repository for this project [Character Share](https://github.com/reltoom/Character-Ideas).
2. In the upper right hand area of the screen, click the 'Fork' button.
3. Then when the menu drops down, click 'Create New Fork'. (If you are the owner of a repository, you cannot fork.) 

#### How to Clone in Github

If you want to clone this repository:

1. Go to the repository for this project [Character Share](https://github.com/reltoom/Character-Ideas).
3. Click on the green 'Code' button and then select how you would like to clone: HTTPS, SSH or GitHub CLI (under the 'local' tab). 
4. Either copy the desired code or click to open with another program from the list below the code.
4. Open your code editor and go to 'Clone Repository' usually under 'File'.
5. Paste if your code and then 'Clone'.

## Testing
## Manual Testing

## Validator Test

[Pep8 Python Validator](https://pep8ci.herokuapp.com/) 

[W3C](https://validator.w3.org/) 

[JShint](https://jshint.com/) 


## Credits

### Code Used


### Acknowledgments

Thank you to my daughter and wife for helping support me through my studies.
