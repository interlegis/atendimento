# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_remove_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]