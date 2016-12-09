# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profession', models.CharField(max_length=255)),
                ('about', models.TextField(max_length=1024)),
                ('image', models.FileField(upload_to='/Users/type3/Projects/michael_brooks/brooks/settings/../../media')),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('snapchat', models.URLField(null=True)),
                ('pinterest', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=1024)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_testimonial_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
