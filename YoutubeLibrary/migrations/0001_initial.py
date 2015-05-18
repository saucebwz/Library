# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=1500)),
                ('thumb_url', models.URLField(max_length=120)),
                ('link', models.URLField(max_length=120)),
                ('added_data', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(to='YoutubeLibrary.Category', related_name='category')),
            ],
        ),
    ]
