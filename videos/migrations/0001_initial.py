# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('air_date', models.DateField()),
                ('host', models.URLField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Show')),
            ],
        ),
    ]