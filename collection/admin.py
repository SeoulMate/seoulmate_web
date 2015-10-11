from django.contrib import admin

# Register your models here.
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['user','title','content',"link","photo",'objectId']}),
	('Date Information',{ 'fields': ['createdAt'], 'classes': ['collapse']}),]

	list_display = ('user', 'title','content','photo','thumb','link','objectId','post_slug')
	list_editable = ('title', 'content','photo','post_slug','objectId')
	list_filter = ['updatedAt']
	search_fields = ['title', 'content']

# admin.site.register(Collection,CollectionAdmin)
admin.site.register(Collection)
