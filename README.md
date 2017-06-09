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

Oh, it's coming. Just give me a little bit while I write this code here.

To load dummy data into the sqlite database, make sure to migrate the database first. Then run this command:

`python manage.py loaddata data.json`

That will give you all of the test data I was using for this project.