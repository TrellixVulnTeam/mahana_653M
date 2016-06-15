# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(blank=True, db_column='StockLocationID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.StockLocation', verbose_name='Store location'),
        ),
    ]
