from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Collection

categories = {0: 'Korean Language', 1: 'News', 2: 'Media', 3: 'Jobs & Internships', 4:'Scholarships', 5:'Tourism', 6:'History & Culture', 7:'Social Media'}


def index(request):
	posts = Collection.objects.order_by('-createdAt')

	context = {'posts': posts,'categories': categories}
	return render(request,'collection/collection_home.html', context)

def postView(request,object_id):
	post = get_object_or_404(Collection,objectId=object_id)
	return render(request,'collection/singlepost.html', {'post':post, 'category': categories[post.category]})

def koreanView(request,object_id):
    post = get_object_or_404(Collection,objectId=object_id)
    return render(request,'collection/singlepost.html', {'post':post, 'category': categories[post.category]})

@csrf_exempt
def boardpost(request):
    if request.method == "POST":
    	# print ('Raw Data: "%s"' % request.body)
        data = json.loads(request.body)
        collection = Collection.create(data['title'],data['content'],data['link'],data['position'],data['category'],data['thumb'],data['photo'],data['user'], data['objectId'])
        collection.save()
        return HttpResponse("SUCCESS")
        # return  render(request, 'blog/blog_home.html',context_instance=RequestContext(request))
    else:
    	return  render(request, 'collection/collection_home.html',context_instance=RequestContext(request))