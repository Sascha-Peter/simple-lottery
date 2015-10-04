# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('address_1', models.CharField(max_length=240, verbose_name='address line one')),
                ('address_2', models.CharField(blank=True, max_length=240, verbose_name='address line two')),
                ('street', models.CharField(max_length=240)),
                ('city', models.CharField(max_length=240)),
                ('postcode', models.CharField(help_text='Supported formats: W2 3PR, HG1 5EY , LS168AG', max_length=7)),
                ('county', models.CharField(blank=True, max_length=140)),
                ('nation', models.CharField(blank=True, max_length=140)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
