# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20171016_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webusers',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='webusers/'),
        ),
    ]