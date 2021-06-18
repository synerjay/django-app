
from django.urls import path
from . import views


app_name = 'articles' # this is to prevent confusion for the name="list". if you have another app that uses name="list" then this will help differentiate

urlpatterns = [
    path('', views.article_list, name="list"), # the name urls seem liek a variable that helps to simplify calling the root in another function
    path('<slug:slug>/', views.article_detail, name="detail") # similar to params in node express
]



# SLUGS IN MODERN DJANGO a.k.a. similar to params in Node.js !!

# This has been significantly changed in Django 3, this could be done like this:
# path('<slug:slug>/', views.article_detail), YOU MUST ADD the forward slash
# where the first slug "<slug" is the type of the passed parameter which is a slug in our case, 
# and the second slug ":slug>" is the name of the parameter which could be any name; "abc", "the_slug", etc.