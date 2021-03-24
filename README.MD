# Django Tables Test proj:

Example Django proj for tables reservation with tests

Usage writen for Linux/Ubuntu and assumes you have
installed postgres database (https://www.postgresql.org/)

Usage: 

1). python3 -m venv env

2). source env/bin/activate

3). cd Restaraunt-proj

4). python -m pip install -r requirements.txt

5). in /tables/settings.ini change:  
    a) SECRET_KEY=  *Your generated key*
    b) DB_NAME= *Your database name*
    c) DB_USER= *Your database user name*
    d) DB_PASSWORD= *If your db user has pass, put it here*

6). python manage.py makemigrations

7). python manage.py migrate

8). python manage.py createsuperuser

9). python manage.py test

10). python manage.py runserver

11). in browser http://127.0.0.1:8000/admin (login and password of superuser from 8)

