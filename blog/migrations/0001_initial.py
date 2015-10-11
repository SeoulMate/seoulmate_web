# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('cat_title', models.CharField(max_length=250, default='social')),
                ('cat_pos', models.IntegerField(default=7)),
                ('cat_description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('post_author', models.CharField(max_length=250)),
                ('post_author_photo', models.ImageField(upload_to='posts/author', blank=True)),
                ('post_title', models.CharField(max_length=400)),
                ('post_photo', models.ImageField(upload_to='posts', blank=True)),
                ('post_content', models.TextField()),
                ('post_slug', models.SlugField(unique=True, max_length=500)),
                ('post_modified', models.DateTimeField(verbose_name='date modified', default=django.utils.timezone.now)),
                ('post_published', models.DateTimeField(verbose_name='date published', default=django.utils.timezone.now)),
                ('post_type', models.CharField(max_length=200)),
                ('is_live', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('post', models.ForeignKey(to='blog.Post', related_name='tags')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
