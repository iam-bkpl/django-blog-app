from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog, name='blog'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
