from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
from .models import University 


def index(request):
	if request.method == "GET":
		q = request.GET.get('search')
		if q:
			results = University.objects.filter(Q(name_eng__icontains=q) | Q(intro__icontains=q) | Q(name_kor__icontains=q)).order_by('createdAt')
			context = {'unis': results}
			return render(request,'daehakgyo/university_home.html', context)
		else: 
			unis = University.objects.order_by('rank')
			context = {'unis': unis}
			return render(request,'daehakgyo/university_home.html', context)


def postSlug(request,slug):
	uni = get_object_or_404(University,uni_slug=slug)
	return render(request,'daehakgyo/university_single.html', {'uni':uni})

# def search(request):
# 	context = ""
# 	if request.method == "GET":
# 		q = request.GET['search']
# 		results = University.objects.filter(Q(name_eng__icontains=q) | Q(intro__icontains=q) | Q(name_kor__icontains=q)).order_by('createdAt')
# 		context = {'unis': results}
# 	return render(request,'daehakgyo/university_home.html', context)
