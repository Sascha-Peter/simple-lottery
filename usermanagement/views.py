"""This file contains all user related views.

author: Sascha Peter <sascha.o.peter@gmail.com>
version: 0.4.0
since: 2015-10-04
"""
from django.shortcuts import render

from .forms import UserForm, UserProfileForm


def sign_up(request):
    """Handle user sign ups with user and profile form."""
    if request.method == "POST":
        user_form = UserForm(request.POST, prefix="user")
        profile_form = UserProfileForm(request.POST, prefix="userprofile")
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            userprofile = profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return render(request, 'registration/thank_you.html')
    else:
        user_form = UserForm(prefix="user")
        profile_form = UserProfileForm(prefix="userprofile")
    return render(request, 'registration/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
