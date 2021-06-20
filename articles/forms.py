from django import forms
from . import models # we need access to model 

# making a custom form
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']