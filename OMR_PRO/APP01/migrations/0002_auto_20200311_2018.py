# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-03-11 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=16, null=True)),
                ('age', models.IntegerField(default=1, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='userinfo',
        ),
    ]