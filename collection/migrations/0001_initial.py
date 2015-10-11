# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user', models.TextField()),
                ('title', models.TextField()),
                ('photo', models.TextField(null=True, default=None, blank=True)),
                ('thumb', models.TextField(null=True, default=None, blank=True)),
                ('content', models.TextField()),
                ('link', models.TextField(null=True, default=None, blank=True)),
                ('post_slug', models.SlugField(unique=True, max_length=600)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(default=7)),
                ('position', models.IntegerField(default=100)),
                ('objectId', models.TextField()),
                ('is_live', models.BooleanField(default=True)),
            ],
        ),
    ]
