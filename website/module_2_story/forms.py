from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, CharField, TextInput
from module_1_users.models import Story, Tag, Category


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class CategoryForm(ModelForm):

    name = CharField(min_length=3, max_length=250, required=True, widget=TextInput())
    
    class Meta:
        model = Category
        fields = ['name']

class StoryForm(ModelForm):

    title = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    text = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Story
        fields = ['title', 'text']
        exclude = ['tags', 'categories', 'type']
