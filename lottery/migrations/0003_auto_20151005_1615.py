# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_lottery_open_entries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='open_entries',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
