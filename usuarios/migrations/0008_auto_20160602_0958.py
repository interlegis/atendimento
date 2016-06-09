# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20160602_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='conveniado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='responsavel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='habilitado',
            field=models.BooleanField(default=False, verbose_name='Habilitado?'),
        ),
    ]