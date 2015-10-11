# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name_eng', models.CharField(max_length=450)),
                ('name_kor', models.CharField(max_length=450)),
                ('address_eng', models.CharField(max_length=600)),
                ('address_kor', models.CharField(max_length=600)),
                ('rank', models.IntegerField(default=0)),
                ('uni_photo_small', models.ImageField(upload_to='posts/uni')),
                ('uni_photo_banner', models.ImageField(upload_to='posts/uni')),
                ('intro', models.TextField()),
                ('link', models.CharField(max_length=450)),
                ('uni_slug', models.SlugField(unique=True, max_length=600)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('admission_open', models.BooleanField(default=True)),
                ('uni_map', models.TextField(default='')),
                ('airport_route', models.TextField(default='')),
            ],
        ),
    ]
