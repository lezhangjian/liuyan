# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-22 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiuyanModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=60, verbose_name='地址')),
                ('message', models.CharField(max_length=600, verbose_name='留言')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
        ),
    ]
