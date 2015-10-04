"""This file contains all user related forms

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0
@since: 2015-10-04
"""
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.gb.forms import GBPostcodeField

from .models import UserProfile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1",
                  "password2")


class UserProfileForm(ModelForm):
    postcode = GBPostcodeField()

    class Meta:
        model = UserProfile
        exclude = ['user']
