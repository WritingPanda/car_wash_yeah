# Car Wash App

## Challenge criteria:

Please build an application for a car wash business. This is an open ended request, so there are many ways you could do this. However, make sure your application can handle the following:
    
- Your car wash accepts cars and trucks.
- You charge $5 for cars.
- Your charge $10 for trucks.
- Your car wash charges $2 extra if the truck has mud in the bed.
- Your car wash does not accept trucks with the bed let down.
- If the vehicle comes in a second time, they get 50% off.
- If the license plate equals 1111111, the vehicle is stolen and does not get a car wash.
 
Please write your code with a mind to its instructional use.

What I'm using:

* [Python 3.6.1](https://www.python.org/downloads/release/python-361/)
* [Django 1.11.2](https://www.djangoproject.com/)

## Methodology

For this project, I am going to keep it simple and create a minimally viable product. The goal is to meet the requirements in order to make instruction of building the application as easy to understand as possible. The additions of the other elements in Flask offer opportunities for further expansion of the project, if time, but the main goal is to meet the requirements in as simple of a way as possible.

**EDIT**: I am refactoring my code for Django. I got tired of working with all of the different packages in Flask. There was too much that I needed and very little time to get it all together in a short lesson to show someone how to use the web framework to build a simple application. For now, I am going to make it easier on myself and show someone how to use Django instead. It has everything I need and then some.

## Learning Objectives

Since we are working with a microframework, it makes it simpler to breakdown the application into small pieces for people to start using it as soon as they finish the tutorial. Easy to read source code with plenty of comments will help in this regard.

When finished reading the source code or watching the subsequent video (TBD), developers will:

1. Be able to install Django
2. Write a basic application
3. Understand the fundamentals of Python for web development
4. Utilize a development server
5. Write, read, update, and delete data from a database using Django ORM
6. Create models to represent their data
7. Write a simple user interface using HTML and CSS
8. Use a CSS framework like Bootstrap for styling and organizing the presentation layer
9. Inject data into templates using Django templates
10. Work with HTML forms and Django

## Documentation

### Installation

To prepare the project, make sure you are using a virtual environment for Python and are using Python 3.6.1. This project has not been tested with Python 2.7.

Edit the `settings.py` file and add in a 50-character random key and save it to the SECRET_KEY variable or `export SECRET_KEY="something_super_secret"` in bash or `set "SECRET_KEY=something_super_secret"` in Windows command prompt. I usually use this secret key generator for sample secret keys: [http://www.miniwebtool.com/django-secret-key-generator/](http://www.miniwebtool.com/django-secret-key-generator/).

Once your virtual environment is active, run this command to install the additional python packages: `pip install -r requirements.txt`. Make sure you are in the project root before running the command.

Afterwards, you will need to migrate the database, which will also create the SQLite3 database. Run this command: `python manage.py migrate`. 

To create a new superuser, run this command: `python manage.py createsuperuser`. You will be prompted to enter in a username and password for the new super user. This super user account will allow you to log into the application and view the tables and access the admin view.

To load dummy data into the sqlite database, run this command: `python manage.py loaddata data.json`. That will give you all of the test data I was using for this project.

### User Guide

To view the project in the browser, run this command: `python manage.py runserver`. This will start the development server and allow you to view the web application at `http://localhost:8000`.

To access the admin view, navigate to `http://localhost:8000/admin/`. From there, you will be able to control the data in the application. You can use the forms in the New Customer or New Transaction views to create new records in the database, but you can also go into the Admin view and create, edit, and delete the records. There is some business logic associated with the views in the New Customer and New Transaction that will not work in the Admin view, but as a super user, you will be able to perform any action against the database as an administrator. 

Customers will need to be created before transactions can be done. This way, transactions can be associated with specific customers, allowing the application to keep track of the amount a particular customer has spent on car washes and how many times they have visited the location.

If the customer has a vehicle that is stolen, the application will not accept the transaction and notify the user that the vehicle is stolen.

If the customer has a truck that is too muddy, the application will increase the price by $2. 

If the customer's truck bed is down, the application will not accept the transaction and notify the user that the vehicle is unacceptable at the car wash.

## Testing

There is a _severe_ lack of testing in this application, which is something I do want to cover in the future. Testing for Django is pretty robust, so I am looking forward to diving into it and writing tests against the application.
