"""Coyote_GameHub URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls'), name = 'home'),
    url(r'^signup/', include('home.urls'), name = 'signup'),
    url(r'^auth/', include('home.urls'), name = 'auth'),
    url(r'^login/', include('home.urls'), name = 'login'),
    url(r'^game1/', include('home.urls'), name = 'game1'),
    url(r'^logout/', include('home.urls'), name = 'logout'),
    url(r'^game2/', include('home.urls'), name = 'game2'),
    url(r'^game3/', include('home.urls'), name = 'game3'),


]
