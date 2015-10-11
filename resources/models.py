import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    photo = models.ImageField(upload_to='posts/resources',blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/category/%s/" % self.slug

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.slug = slugify(self.title)
    	return super(Category,self).save(*args, **kwargs)

class Resource(models.Model):
	site_title = models.CharField(max_length=500)
	description = models.TextField(default="")
	slug = models.SlugField(max_length=200, unique=True)
	curator = models.CharField(max_length=200)
	writer = models.ForeignKey(User)
	site_url = models.URLField(max_length=300,blank=True)
	tags = models.CharField(max_length=200)
	languages = models.CharField(max_length=300,default="English,Korean")
	updatedAt = models.DateTimeField(auto_now=True)
	createdAt = models.DateTimeField(auto_now_add=True)
	category = models.ManyToManyField(Category)
	objectId = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.site_title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.site_title)
			return super(Resource,self).save(*args, **kwargs)

	@classmethod
	def create(cls,title,desc,curator,writer,site_url,tags,lang,objectId):
		resource = cls(site_title=title,description=desc,curator=curator, \
			writer=writer, site_url=site_url, tags=tags,languages=lang,objectId=objectId)
		return resource






