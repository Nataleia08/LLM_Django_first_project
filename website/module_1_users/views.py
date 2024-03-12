from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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




def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='module_1_user:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='module_1_user:index')
        else:
            return render(request, '/signup.html', context={"form": form})

    return render(request, '/signup.html', context={"form": RegisterForm()})



def loginuser(request):
    if request.user.is_authenticated:
       return redirect(to='module_1_user:index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='module_1_user:index')

        login(request, user)
        return redirect(to='module_1_user:index')

    return render(request, 'ulogin.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='noteapp:main')