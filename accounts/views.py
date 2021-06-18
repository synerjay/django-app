from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

# making the account
def signup_view(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save() # returns a user info
        login(request, user)
        return redirect('articles:list')
    else:
      form = UserCreationForm() # this is an instance of the form which below we will send down to the template
    return render(request, 'accounts/signup.html', {'form':form})

# logging the user in
def login_view(request): # name ur login  views with login_views
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST) # we name data = request.POST because it is not he first instance of the data??
      if form.is_valid():
        user = form.get_user() # retrieve user informatio when its trying to login
        login(request, user) # logins the user
        return redirect('articles:list')
    else: 
      form = AuthenticationForm() # django-made login form
    return render(request, 'accounts/login.html', {'form': form}) # inject the form into the front end

#logout users
def logout_view(request):
    # always make a POST request to logout and NOT a GET request
    if request.method == 'POST':
       logout(request)
       return redirect('articles:list')