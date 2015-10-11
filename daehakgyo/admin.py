from django.contrib import admin

# Register your models here.
from .models import University



class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['name_eng','name_kor',"intro",'address_eng',"address_kor","rank","uni_photo_small","uni_photo_banner" \
		,"link","admission_open","uni_map","airport_route"]})]

	list_display = ('name_eng','name_kor',"intro",'address_eng',"address_kor","rank","uni_photo_small","uni_photo_banner" \
		,"link","admission_open","uni_map","airport_route","uni_slug")
	list_editable = ('name_eng','name_kor',"intro",'address_eng',"address_kor","rank","uni_photo_small","uni_photo_banner" \
		,"link","admission_open","uni_map","airport_route","uni_slug")
	list_filter = ['name_eng']
	search_fields = ['name_eng', 'name_kor']

# admin.site.register(University,UniversityAdmin)
admin.site.register(University)
