import datetime

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Collection(models.Model):
	user = models.TextField()
	title = models.TextField()
	photo = models.TextField(default=None, blank=True, null=True)
	thumb = models.TextField(default=None, blank=True, null=True)
	content = models.TextField()
	link = models.TextField(default=None, blank=True, null=True)
	post_slug = models.SlugField(max_length=600,unique=True)
	updatedAt =  models.DateTimeField(auto_now=True)
	createdAt =  models.DateTimeField(auto_now_add=True)
	category = models.IntegerField(default=7)
	position  = models.IntegerField(default=100)
	objectId = models.TextField()
	is_live = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def save(self):
		if not self.id:
			self.createdAt = timezone.now()
			self.post_slug = slugify(self.title)
		self.updatedAt = datetime.datetime.now()
		return super(Collection,self).save()

	@classmethod
	def create(cls,title,content,l,pos,cat,t,p,u,objectId):
		board = cls(title=title,content=content,link=l,position=pos,category=cat,thumb=t,photo=p,user=u,objectId=objectId)
		return board





# class Category(models.Model):
# 	post = models.ForeignKey(Post)
# 	cat_title = models.CharField(max_length=250, default="social")
# 	cat_pos = models.IntegerField(default=7)
# 	cat_description  = models.CharField(max_length=400)

# 	def __str__(self):
# 		return self.cat_title

# # Declare the ForeignKey with related_query_name
# class Tag(models.Model):
#     post = models.ForeignKey(Post, related_name="tags")
#     name = models.CharField(max_length=255)

