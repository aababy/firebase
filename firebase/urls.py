#coding:utf-8

"""firebase URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from firebase.settings import MEDIA_ROOT
from storage import views

urlpatterns = [
    url(r'', admin.site.urls),
    url(r'^admin/', admin.site.urls),

    #ajax 的都要加到这里
    url(r'^ajax/message/', views.ajax_message, name='ajax_message'),
    url(r'^ajax/publish/', views.ajax_publish, name='ajax_publish'),
    url(r'^ajax/get_graphs/', views.ajax_get_graphs, name='ajax_get_graphs'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
