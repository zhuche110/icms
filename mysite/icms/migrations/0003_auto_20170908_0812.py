# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icms', '0002_auto_20170908_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='source',
            field=models.CharField(default='\u539f\u521b', max_length=100, verbose_name='\u6765\u6e90'),
        ),
    ]
