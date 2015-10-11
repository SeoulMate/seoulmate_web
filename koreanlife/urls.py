from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^kpost$', views.koreanpost, name='koreanpost'),
    url(r'^post/(?P<object_id>[a-zA-Z0-9]+)/$', views.koreanView, name='koreanView'),
    url(r'^(?P<object_id>[a-zA-Z0-9]+)/$', views.koreanView, name='koreanView'),
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<slug>[-_\w]+)/$', views.postSlug, name = 'postSlug'),
]
