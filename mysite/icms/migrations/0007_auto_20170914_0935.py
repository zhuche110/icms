# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-14 01:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icms', '0006_auto_20170911_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='uploadfiles',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='\u4e0a\u4f20\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='category',
            name='orderby',
            field=models.IntegerField(default=0, verbose_name='\u6392\u5e8f'),
        ),
    ]
