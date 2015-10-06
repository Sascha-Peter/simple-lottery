# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0006_auto_20151005_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='status',
            new_name='winner',
        ),
        migrations.AlterField(
            model_name='lottery',
            name='open_entries',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
