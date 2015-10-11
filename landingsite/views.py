from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.mail import send_mail, BadHeaderError
from blog.models import Post
from collection.models import Collection

categories = {0: 'Korean Language', 1: 'News', 2: 'Media', 3: 'Jobs & Internships', 4:'Scholarships', 5:'Tourism', 6:'History & Culture', 7:'Social Media'}

def index(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        subject = 'Contact us - Seoul Mate website'
        if subject and message and from_email and first_name and last_name:
            try:
                message = message + "\n From : " + from_email
                send_mail(subject, message, from_email, ['seoulmate.me@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
    else :
        collections = Collection.objects.order_by('-createdAt')[:3]
        posts = Post.objects.order_by('-post_published')[:3]
        context = {'posts': posts,'collections':collections,'categories': categories}
        return render(request,'landingsite/index.html', context)

def eula(request):

    context = ""
    return render(request, 'landingsite/end-user-license-agreement.html', context)
