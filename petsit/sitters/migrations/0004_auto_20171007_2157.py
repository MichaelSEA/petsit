# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0003_auto_20171007_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=512),
        ),
    ]
