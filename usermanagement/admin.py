"""This file contains all user admin related classes.

author: Sascha Peter <sascha.o.peter@gmail.com>
version: 0.4.0
since: 2015-10-04
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import StackedInline

from .models import User, UserProfile


class UserProfileInline(StackedInline):
    """Profile inline for users."""

    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    """User admin panel."""

    inlines = (UserProfileInline, )


class UserProfileAdmin(admin.ModelAdmin):
    """User profile admin panel."""

    model = UserProfile

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
