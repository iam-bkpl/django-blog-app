from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('postComment', views.postComment, name='postComment')
   
]