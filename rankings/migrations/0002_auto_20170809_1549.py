# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='review',
            name='beer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='rankings.Beer'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Alcohol by Volume'),
        ),
    ]