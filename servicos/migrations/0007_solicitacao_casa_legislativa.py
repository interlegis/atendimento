# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 13:01
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (u'servicos', u'0006_auto_20160603_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name=u'solicitacao',
            name=u'casa_legislativa',
            field=models.CharField(default=u'casa1', max_length=200, verbose_name=u'Casa Legislativa'),
            preserve_default=False,
        ),
    ]
