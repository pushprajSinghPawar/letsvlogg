*****************steps to installprojecton your system**********

************************letsblog*********************************
*****************************************************************
------ABOUT LETSBLOGS:>
A blogging website built using Django framework. It is designed for publishing blogs and creating and environment so that there can be interactions between bloggers and readers.
Features include engagement through comments ,serach engine inbuilt , tagging on posts etc.

-----Installation needed to be done:>
Python and Django need to be installed

<<<<<<< HEAD
-----Install django project from github link :> https://github.com/pushprajSinghPawar/letsblog.git
=======
install django project from github link : https://github.com/pushprajSinghPawar/G14-Minor-Project-sem.git
>>>>>>> 9f0452d3ad48217eec5d0454e3f078bfe83c6ab5

-----Installing pip
pip is the reference Python package manager. 
It is used to install and update packages. 
You will need to make sure you have the latest version of pip installed.

> python3 -m pip install --user --upgrade pip

> python3 -m pip --version

-------Create virtual environment :>
Create a virtual environment for the django modules :>
virtualenv is used to manage Python packages for different projects.
Using virtualenv allows you to avoid installing 
Python packages globally which could break 
system tools or other projects.
You can install virtualenv using pip.

> python3 -m pip install --user virtualenv
> create vitualenv (name of virtual environment)

> pip install django

--------These will be requirements.txt :>
asgiref==3.5.0
dj-database-url==0.5.0
Django==4.0.1
django-heroku==0.3.1
gunicorn==20.1.0
psycopg2==2.9.3
sqlparse==0.4.2
tzdata==2021.5
whitenoise==6.0.0

---------Install all these with running  command:>

> pip3 install -r requirements.txt
Set Database (Make Sure you are in directory same as manage.py)

> python manage.py makemigrations
> python manage.py migrate


----------Creating an admin user :>

> python manage.py createsuperuser. Enter your desired username and press enter.
> Username: admin
(You will then be prompted for your desired email address:)
> Email address: admin@example.com. ...
> Password: ********** Password (again): *********
> Superuser created successfully.

now admin will be able to acess the databse and permissions related things.

> python manage.py runserver
Then go to the browser and enter the url http://127.0.0.1:8000/

After all these steps , you can start testing and developing this project.
That's it! Happy Coding!