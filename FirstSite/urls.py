"""
URL configuration for FirstSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  .import views
from django.http import HttpResponse
from register import views as v
from django.utils import timezone
import django_ckeditor_5.views as ck_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/', include('home.urls')),
     path('inbox/notifications/', include('notifications.urls', namespace='notifications')),
    #  path('tinymce/', include('tinymce.urls')),
     path("ckeditor5/", include('django_ckeditor_5.urls')),
     path("/ckeditor5/image_upload/", ck_views.upload_file),
     
]
