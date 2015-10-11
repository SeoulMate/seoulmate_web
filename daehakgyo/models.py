import datetime

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class University(models.Model):
	name_eng = models.CharField(max_length=450)
	name_kor = models.CharField(max_length=450)
	address_eng = models.CharField(max_length=600)
	address_kor = models.CharField(max_length=600)
	rank = models.IntegerField(default=0)
	uni_photo_small = models.ImageField(upload_to='posts/uni')
	uni_photo_banner = models.ImageField(upload_to='posts/uni')
	intro = models.TextField()
	link = models.CharField(max_length=450)
	uni_slug = models.SlugField(max_length=600,unique=True)
	updatedAt =  models.DateTimeField(auto_now=True)
	createdAt =  models.DateTimeField(auto_now_add=True)
	admission_open = models.BooleanField(default=True)
	uni_map = models.TextField(default="")
	airport_route = models.TextField(default="")

	def __unicode__(self):
		return self.name_eng + " | " + self.name_kor 

	def save(self):
		if not self.id:
			self.uni_slug = slugify(self.name_eng)
		# self.updatedAt = datetime.datetime.now()
		return super(University,self).save()

	# @classmethod
	# def create(cls,title,content,l,pos,cat,t,p,u,objectId):
	# 	uni = cls(title=title,content=content,link=l,position=pos,category=cat,thumb=t,photo=p,user=u,objectId=objectId)
	# 	return board
