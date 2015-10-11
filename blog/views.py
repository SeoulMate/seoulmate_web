from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from .models import Post


def index(request):
	posts = Post.objects.order_by('-post_published')
	context = {'posts': posts}	 
	# return HttpResponse(template.render(context))
	return render(request,'blog/blog_home.html', context)

def postView(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	return render(request,'blog/singlepost.html', {'post':post})

def postSlug(request,slug):
	post = get_object_or_404(Post,post_slug=slug)
	return render(request,'blog/singlepost.html', {'post':post})

@csrf_exempt
def boardpost(request):
    if request.method == "POST":
    	# print ("post method")
    	# print ('Raw Data: "%s"' % request.body)
        title = request.POST.get('title','NOTHING')
        # print (title)
        return HttpResponse("SUCCESS")
        # return  render(request, 'blog/blog_home.html',context_instance=RequestContext(request))
    else:
    	return  render(request, 'blog/blog_home.html',context_instance=RequestContext(request))