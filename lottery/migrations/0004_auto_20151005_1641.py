# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_auto_20151005_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='winner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, related_name='lottery_winner', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
