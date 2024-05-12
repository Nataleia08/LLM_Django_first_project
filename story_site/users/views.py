from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm, SentMessageForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile


def index(request):
    # template = loader.get_template('index.html')
    return render(request, 'index.html') 

@login_required
def profile(request):
    prof = request.user
    return render(request, "profile.html", {"prof": prof})

def contacts(request):
    if request.method == 'POST':
        form = SentMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            return render(request, 'contacts.html', {'form': form})

    return render(request, 'contacts.html', {'form': SentMessageForm()})


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            return render(request, 'signup.html', context={"form": form})

    return render(request, 'signup.html', context={"form": RegisterForm()})



def loginuser(request):
    if request.user.is_authenticated:
       return redirect(to='index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='login')

        login(request, user)
        return redirect(to='index')

    return render(request, 'login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='index')