from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader



def index(request):
    # template = loader.get_template('index.html')
    return render(request, 'index.html') 

def story(request):
    return render(request, "story.html")

def bot_translater(request):
    return render(request, "translater.html")

def examples(request):
    return render(request, "examples.html")

def my_project(request):
    return render(request, "my_project.html")

def ukrainian_story(request):
    return render(request, "ukrainian_story.html")

def traveling_story(request):
    return render(request, "traveling_story.html")

def contacts(request):
    return render(request, "contacts.html")