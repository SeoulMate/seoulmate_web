# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeinKorea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=450)),
                ('photo', models.TextField(null=True, blank=True, default=None)),
                ('thumb', models.TextField(null=True, blank=True, default=None)),
                ('content', models.TextField()),
                ('link', models.TextField(null=True, blank=True, default=None)),
                ('post_slug', models.SlugField(unique=True, max_length=600)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=200)),
                ('objectId', models.TextField()),
                ('is_live', models.BooleanField(default=True)),
            ],
        ),
    ]
