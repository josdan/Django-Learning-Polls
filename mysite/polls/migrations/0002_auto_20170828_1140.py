# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choise',
            old_name='Choice_text',
            new_name='choice_text',
        ),
    ]
