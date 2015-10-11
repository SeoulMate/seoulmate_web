# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('photo', models.ImageField(upload_to='posts/resources', blank=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('site_title', models.CharField(max_length=500)),
                ('description', models.TextField(default='')),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('curator', models.CharField(max_length=200)),
                ('site_url', models.URLField(blank=True, max_length=300)),
                ('tags', models.CharField(max_length=200)),
                ('languages', models.CharField(default='English,Korean', max_length=300)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('objectId', models.CharField(null=True, blank=True, max_length=100)),
                ('category', models.ManyToManyField(to='resources.Category')),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
