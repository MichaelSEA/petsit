# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0005_auto_20171007_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='name',
            field=models.CharField(db_index=True, max_length=512),
        ),
    ]
