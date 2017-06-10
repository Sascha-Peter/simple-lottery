"""simple_lottery URL Configuration.

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
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve
from lottery import urls as lottery_urls
from django.contrib.auth.views import logout
from django.contrib.auth import urls
from usermanagement.views import sign_up
from lottery.admin import show_lottery_winner

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),
    url(r'^lottery/', include(lottery_urls)),
    url(r'^logout/$', logout,
        {'next_page': '/'},
        name="logout"),
    url('^', include(urls)),
    url('^sign-up/', sign_up, name="sign-up"),
    url(r'^admin/lottery_winner/', show_lottery_winner,
        name="winner-list"),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT, }), ]
