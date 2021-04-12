# Project name: Vy's Recipes

## Project link: 

## Project description:
**Vy's Recipes** is an web application also mobile friendly about Vietnamese Food Recipes. You can access to tons of recipes from Vietnamese Specialties to Vietnamese streetfoods like Pho, Banh Mi, Bun Bo, Hu tiu Bo kho, Banh trang nuong (Vietnamese Pizza)...You can also save the recipes that you like when you register to the website.


## Technologies used:
- Language: HTML, CSS, JS, Python
- Framework: Django, Materialize
- Database: Postgresql
- Deployment on: Netlify 

## Installation steps:
- python3 -m venv .env
- source .env/bin/activate
- createdb vyrecipes
- pip install --upgrade pip (if upgrading required)
- pip3 install psycopg2-binary
- pip3 install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py runserver

**In this project, I installed:**
- python -m pip install Pillow 

**Remember to add superuser admin**
- python3 manage.py createsuperuser

## User stories:
**User should be able to:**
- See all the latest receipes in homepage.
- Click on Read More to see the receipe detail.
- Sign up a new account.
- Log in if he/she has already registered

**After login, user should be able to:**
- Be redirected to their public profile page
- Change his/her name
- Change his/her email
- Save the reciepe that he/she likes

## Wireframes:

**Homepage**

<img src="images/home.png">

<img src="images/home1.png">

**Receipe page**

<img src="images/receipe.png">

**About page**

<img src="images/about.png">

**Profile Page**

<img src="images/profile.png">


## Entity relationship diagram:

<img src="images/erd.png">

## Futute features:
**After login, user shouls be able to:**
- Add comments in the receipe page
- Delete comments in the receipe page
