# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0007_stay_dogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='overall_sitter_rank',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
