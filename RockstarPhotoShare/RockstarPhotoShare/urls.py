"""RockstarPhotoShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns, include
from django.contrib import admin


urlpatterns =patterns('',url(r'^$', 'rockstar.views.home', name='home'),
                     url(r'^admin/',include(admin.site.urls)),
                     url(r'^register/$', 'rockstar.views.register', name='register'),
                     url(r'^login/$', 'rockstar.views.user_login', name='login'),
                     url(r'^login/rockstar/logout/', 'rockstar.views.user_logout', name='logout'),
                     url(r'^index/$', 'rockstar.views.index', name='index'),
                     url(r'^login/rockstar/index', 'rockstar.views.index'),)

