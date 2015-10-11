from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import LifeinKorea



def index(request):
	posts = LifeinKorea.objects.order_by('-createdAt')

	context = {'posts': posts}
	return render(request,'lifeinkorea/lifeinkorea_home.html', context)


def koreanView(request,object_id):
    post = get_object_or_404(LifeinKorea,objectId=object_id)
    return render(request,'lifeinkorea/singlepost.html', {'post':post})

def postSlug(request,slug):
	post = get_object_or_404(LifeinKorea,post_slug=slug)
	return render(request,'lifeinkorea/singlepost.html', {'post':post})

@csrf_exempt
def koreanpost(request):
    if request.method == "POST":
    	# print 'Raw Data: "%s"' % request.body
        data = json.loads(request.body)
        # t, c,l, pos,cat,t,p,u
        # print "title : " + data['title']
        korean = LifeinKorea.create(data['title'],data['content'],data['link'],data['tags'],data['thumb'],data['photo'],data['user'], data['objectId'])
        # print collection
        korean.save()
        # print collection.id
        return HttpResponse("SUCCESS")
        # return  render(request, 'blog/blog_home.html',context_instance=RequestContext(request))
    else:
    	return  render(request, 'lifeinkorea/lifeinkorea_home.html',context_instance=RequestContext(request))
