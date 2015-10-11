from django.contrib import admin

# Register your models here.
from .models import Post,Category, Tag

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

class TagInline(admin.TabularInline):
    model = Tag
    extra = 3

class PostAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['post_author','post_author_photo','post_title',"post_content","post_photo"]}),
	('Date Information',{ 'fields': ['post_published'], 'classes': ['collapse']}),]

	list_display = ('post_author', 'post_title','post_content','post_photo','post_published','post_modified','post_slug')
	list_editable = ('post_title', 'post_content','post_photo','post_slug')
	list_filter = ['post_modified','post_published']
	search_fields = ['post_title', 'post_content']
	inlines = [CategoryInline, TagInline]

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)