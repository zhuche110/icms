# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 09:39
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icms', '0003_auto_20170908_0812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u680f\u76ee\u5206\u7c7b', 'verbose_name_plural': '\u680f\u76ee\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='entries',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterField(
            model_name='entries',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=60000, verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
    ]
