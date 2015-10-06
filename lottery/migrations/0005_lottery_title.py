# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_auto_20151005_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='title',
            field=models.CharField(max_length=140, blank=True),
        ),
    ]
