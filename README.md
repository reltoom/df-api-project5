# Meal Share Backend drf.

This is my Back-End Django REST Framework for my PP5, Meal Share. 

Visit the deployed Back-End here: [Meal Share Back-End](https://df-api-project5-f27c63867984.herokuapp.com/)
    - This would mainly be to log in as admin to the site.

## CONTENTS

* [Planning Of Models](#planning-of-models)
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

## Planning of Models
My ERD which I planned out for my Models [ERD](readme_assets/images/erd.png)

## Technologies 

### Languages
For Meal Share Back-end
* Python - Used to create my Back-End code.

###  Websites & Programs 

* [DjangoREST framework](https://www.django-rest-framework.org/)Guide and reference for code.
* [Github](https://github.com/) - Created repository and stored files here after commits. 
* [Heroku](https://heroku.com/) - For deploying both the Back-End and Front-End of Meal Share.
* [Microsoft Visual Studio](https://visualstudio.microsoft.com/) - Wrote code and did commits to Github from here.
* [W3 School](https://www.w3schools.com/) Read and used as a guide for some code.
* [Chatgpt](https://chat.openai.com/) - Used to help identify problems in code and possible way to solve them.
* [Visual Paradigm](https://online.visual-paradigm.com/) - Used to draw my ERD diagram digitally

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
    * Search for your Back-End repo and then 'Connect'
    * Click the 'Manual Deploy' to deploy manually after every update on GitHub, or you can activate the 'Automatic Deployement' which will try to deploy after every new push to GitHub.
    * Now that it is deployed, you can click on the 'Open App' button in the top right hand off the screen in Heroku.


#### How to Fork in Github

If you want to fork this repository in Github:

1. Go to the repository for this project [df-api-project5](https://github.com/reltoom/df-api-project5).
2. In the upper right hand area of the screen, click the 'Fork' button.
3. Then when the menu drops down, click 'Create New Fork'. (If you are the owner of a repository, you cannot fork.) 

#### How to Clone in Github

If you want to clone this repository:

1. Go to the repository for this project [df-api-project5](https://github.com/reltoom/df-api-project5).
3. Click on the green 'Code' button and then select how you would like to clone: HTTPS, SSH or GitHub CLI (under the 'local' tab). 
4. Either copy the desired code or click to open with another program from the list below the code.
4. Open your code editor and go to 'Clone Repository' usually under 'File'.
5. Paste if your code and then 'Clone'.

## Testing
## Manual Testing
<details><summary><b>Manual Testing<b></summary>

| | | |
|:-------:|:--------|:--------|
| Log in | After creating superuser, log in | Using correct username and password logs the superuser into the API. |
| Wrong login info | Tried to log it with wrong info | Error messages show that I need to log it with correct username or password. |
| Admin Page | Appending '/admin' to the end of the url | Takes the superuser to the admin page where it shows all relevant apps: Users, Books, Posts, Profiles etc. |
| Books | Clicked on Books in admin panel | Shows list of current Books that have been created. Also button for adding a book. |
| Add Book | Clicked on 'Add book' | Brings up the add book form. Am able to choose which user, Title, Author and Link. Buttons for Save are present and if clicked save the newly created book to the database, shows up in the list of books. Title and Author field are required and will show error messages if left blank. |
| Book Delete | Click on a book from the book list | Here the admin can edit the book that has been created and save or click the 'Delete' button to delete the book from the database. |
| Posts | Clicked on Posts in admin panel | Displays a list of posts that have been created(by title) as well as the 'Add Post' button. |
| Add Post | Click the 'Add Post' button | Takes admin to the add post form. Admin can fill in the form, recipe name is a required field to be able to save post. Saving adds it to the list of Posts |
| Post Delete | Click on a created Post in the list | Brings up the 'Add Post' form but prefilled with the posts details. Here the admin can edit information about it or click the 'Delete' button which will delete the post from the database. |
| Profiles | Click the Profiles in the admin panel | Brings up a list of current profiles that users have created. |
| Add Profile | Click the add profile button | The admin is able to create users, and fill in their profile info and image. Saving it will add the new user to list of users |
| Delete Profile | Click a current Username in the profile view | This brings up the users profile info to be edited, or 'Delete' button will remove the profile from database. |

The Back-End for Meal Share works as it should.
</details><br/>

## Validator Test
I have run this Back-End project through validator testing.
[Pep8 Python Validator](https://pep8ci.herokuapp.com/) -- All clear, no errors were found in my python code.

## Credits

### Code Used
I used the Back-End code from the Moments walkthrough and then changed it to fit Meal Share. 

### Acknowledgments
Thank you to my daughter and wife for helping support me through my studies.
