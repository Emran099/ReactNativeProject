Create / install Virtual enviroment

python -m venv .venv

Activate Virtual 
.venv\Scripts\activate

Intsall Django
pip install django

install rest framework

pip install djangorestframework


check django-admin
django-admin


django start/create project (. current dir)
django-admin startproject DjangoRestAPI .


run server
python manage.py runserver


You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

python manage.py migrate


ADMIN Page enable

create super user
python manage.py createsuperuser


Create Model in Models.py

from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

settigs.py 
installed app Add models

now create model by command
python manage.py makemigrations DjangoRestAPI

migrate before run server
python manage.py migrate 




