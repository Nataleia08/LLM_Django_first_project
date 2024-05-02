from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput
from .models import Message


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class SentMessageForm(ModelForm):

    contacts = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    text = CharField(min_length=10, max_length=250, required=True, widget=TextInput())

    class Meta:
        model = Message

        fields = ['contacts', 'text']