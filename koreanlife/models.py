import datetime

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify



class LifeinKorea(models.Model):
	user = models.CharField(max_length=200)
	title = models.CharField(max_length=450)
	photo = models.TextField(default=None, blank=True, null=True)
	thumb = models.TextField(default=None, blank=True, null=True)
	content = models.TextField()
	link = models.TextField(default=None, blank=True, null=True)
	post_slug = models.SlugField(max_length=600,unique=True)
	updatedAt =  models.DateTimeField(auto_now=True)
	createdAt =  models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=200)
	objectId = models.TextField()
	is_live = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = "lifeinkorea"

	def __str__(self):
		return self.title

	def save(self):
		if not self.id:
			self.createdAt = timezone.now()
			self.post_slug = slugify(self.title)
		self.updatedAt = datetime.datetime.now()
		return super(LifeinKorea,self).save()

	@classmethod
	def create(cls,title,content,l,tags,t,p,u,objectId):
		korean = cls(title=title,content=content,link=l,tags=tags,thumb=t,photo=p,user=u,objectId=objectId)
		return korean
