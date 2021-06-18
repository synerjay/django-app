# In a new app, you must make a urls.py file and then import these two

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup_view, name="signup"), 
  path('login/', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout")
]