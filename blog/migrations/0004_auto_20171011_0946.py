# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170930_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Post',
        ),
    ]
