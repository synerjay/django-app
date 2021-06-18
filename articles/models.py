from django.db import models
from django.urls.converters import SlugConverter

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # automatically add the date of NOW
    thumb = models.ImageField(default='default.png', blank=True) # data field for image / default image if no image / blank =True - it can be a blank field and not requried
    # add in author later

    # the function below makes the title of each instance of the article visible in the Query Article.objects.all()
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'

# The Command Lines for Migrations
  # python manage.py makemigrations    <---- make a migration file
  # python manage.py migrate   <--- migrate the changes to the database