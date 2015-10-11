from django.contrib import admin
from .models import Resource,Category

class ResourceAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['writer','site_title','description',"curator","site_url",'tags''languages']}),
	('Date Information',{ 'fields': ['createdAt'], 'classes': ['collapse']}),]

	list_display = ('writer','curator', 'site_title','description','site_url','tags','languages')
	list_editable = ('writer','curator','site_title', 'description','site_url','tags','languages')
	list_filter = ['updatedAt']
	search_fields = ['site_title', 'description']

admin.site.register(Category)
admin.site.register(Resource,ResourceAdmin)


