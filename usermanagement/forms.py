"""This file contains all user related forms.

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.4.0
@since: 2015-10-04
"""
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.gb.forms import GBPostcodeField

from .models import UserProfile


class UserForm(UserCreationForm):
    """User creation form."""

    class Meta:
        """Meta definition for user form."""

        model = User
        fields = ("username", "first_name", "last_name", "email", "password1",
                  "password2")


class UserProfileForm(ModelForm):
    """User profile form."""

    postcode = GBPostcodeField()

    class Meta:
        """Meta defition for user profile form."""

        model = UserProfile
        exclude = ['user']
