"""This file contains all user related models

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.1
@since: 2015-10-04
"""
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """This model defines the user profile"""
    user = models.OneToOneField(User)
    address_1 = models.CharField("address line one", max_length=240)
    address_2 = models.CharField("address line two", max_length=240,
                                 blank=True)
    street = models.CharField(max_length=240)
    city = models.CharField(max_length=240)
    postcode = models.CharField(max_length=7,
                                help_text='Supported formats: W2 3PR, ' +
                                'HG1 5EY , LS168AG')

    def __str__(self):
        return self.user.username
