from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', views.resource_cat, name = 'resource_cat'),
    url(r'^$', views.index, name='index'),
]
