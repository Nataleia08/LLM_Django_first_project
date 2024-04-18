from django.shortcuts import render

# Create your views here.

def my_project(request):
    return render(request, "my_projects.html")

def bot_translater(request):
    return render(request, "translater.html")