import datetime

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
	post_author = models.CharField(max_length=250)
	post_author_photo = models.ImageField(upload_to='posts/author',blank=True)
	post_title = models.CharField(max_length=400)
	# post_name = models.CharField(max_length=400)
	post_photo = models.ImageField(upload_to='posts',blank=True)
	post_content = models.TextField()
	post_slug = models.SlugField(max_length=500,unique=True)
	post_modified =  models.DateTimeField('date modified',default=timezone.now)
	post_published =  models.DateTimeField('date published',default=timezone.now)
	post_type = models.CharField(max_length=200)
	is_live = models.BooleanField(default=False)

	def __str__(self):
		return self.post_title

	def save(self):
		if not self.id:
			self.post_published = timezone.now()
			self.post_slug = slugify(self.post_title)
		self.post_modified = datetime.datetime.now()
		return super(Post,self).save()


class Category(models.Model):
	post = models.ForeignKey(Post)
	cat_title = models.CharField(max_length=250, default="social")
	cat_pos = models.IntegerField(default=7)
	cat_description  = models.CharField(max_length=400)

	def __str__(self):
		return self.cat_title

# Declare the ForeignKey with related_query_name
class Tag(models.Model):
    post = models.ForeignKey(Post, related_name="tags")
    name = models.CharField(max_length=255)

