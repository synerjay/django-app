from django.contrib import admin
from .models import Article #first import the Article model in here

# Register your models here.

admin.site.register(Article)
# this is how we tell Django to register the models to the admin site