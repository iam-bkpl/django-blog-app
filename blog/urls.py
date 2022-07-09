from django.contrib import admin
from django.urls import path
from . import views
from blog. models import Post
# from .models import BlogComment

urlpatterns = [
    # path('postComment', views.postComment, name='postComment'),
    path('', views.blog, name='blog'),
    path('<str:slug>', views.blogPost, name='blogPost'),


]
