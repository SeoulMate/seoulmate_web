from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt


from .models import Resource,Category


def index(request):
	cats = Category.objects.all()
	context = {'cats':cats}
	return render(request,'resources/resources_home.html',context)

def resource_cat(request,slug):
	cat = get_object_or_404(Category,slug=slug)
	posts = Resource.objects.all().order_by('createdAt')
	category_resources = []
	for post in posts:
		if Category.objects.filter(resource=post):
			category_resources.append(post)
	context = {'posts':category_resources, 'cat' : cat}
	return render(request,'resources/resource_cat_home.html',context)