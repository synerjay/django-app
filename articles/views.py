from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# In order to inject the article model data into the HTML we need to import the article models
# and then render it into the function below

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # goes to the models of the database to find the article with the corresponding slug
    return render(request, 'articles/article_detail.html', {'article': article}) # the article with 'quotations' is like a variable, you can call it whatever u want. With that variable we are sending in the article data


# First we make a variable equal to the Model class and grab the data by .objects.all() method. This will return a list (array)
# then we can add another method to sort the list in an order we want .order_by() anything define 
# the render method takes in a third argument which accepts a dictionary (object) and tells which data to render. In this case the articles variable 