"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^post$', views.boardpost, name='boardpost'),
    url(r'^board/(?P<object_id>[a-zA-Z0-9]+)/$', views.postView, name='postView'),
    url(r'^(?P<object_id>[a-zA-Z0-9]+)/$', views.koreanView, name='koreanView'),
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<slug>[-_\w]+)/$', views.postSlug, name = 'postSlug'),
]
