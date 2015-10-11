"""seoulmateapp URL Configuration

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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^collections/', include('collection.urls', namespace="collection")),
    url(r'^resources/', include('resources.urls', namespace="resources")),
    url(r'^daehakgyo/', include('daehakgyo.urls', namespace="daehakgyo")),
    url(r'^lifeinkorea/', include('koreanlife.urls', namespace="koreanlife")),
	url(r'^end-user-license-agreement/',TemplateView.as_view(template_name='landingsite/end-user-license-agreement.html'),name='end-user-license-agreement'),
    url(r'^privacy-policy/',TemplateView.as_view(template_name='landingsite/privacy-policy.html'),name='privacy-policy'),
    url(r'^contact/thanks/',TemplateView.as_view(template_name='landingsite/thanks.html'),name='thanks'),
    url(r'^contact-us/',TemplateView.as_view(template_name='landingsite/contact_us.html'),name='contact-us'),
    url(r'^help-center/',TemplateView.as_view(template_name='landingsite/help-center.html'),name='help-center'),
    url(r'^$', include('landingsite.urls', namespace="landingsite")),
]

#urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
