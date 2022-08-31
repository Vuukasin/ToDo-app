from pyexpat import model
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django import forms



class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(help_text=False)


    password1 = forms.CharField(help_text=False, label='Password', widget=forms.PasswordInput())

    password2 = forms.CharField(help_text=False, label='Password confirmation', widget=forms.PasswordInput())


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


    username = forms.CharField()

    password = forms.PasswordInput()
    