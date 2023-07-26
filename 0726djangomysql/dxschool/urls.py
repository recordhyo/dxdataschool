"""
URL configuration for dxschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
# 애플리케이션의 views 파일의 내용을 사용할 수 있도록 import
from web0726 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("hi/", views.display),
    path("template/", views.template),
    path("fruits", views.fruits),
    path("detail/<str:itemid>", views.detail)
]
