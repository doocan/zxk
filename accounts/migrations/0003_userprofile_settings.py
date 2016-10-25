# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-25 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161021_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='settings',
            field=models.CharField(choices=[('E', 'Editor'), ('M', 'Markdown')], default='M', max_length=10),
        ),
    ]
