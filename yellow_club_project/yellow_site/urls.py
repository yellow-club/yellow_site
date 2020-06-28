from django.urls import path

from .views import *

urlpatterns = [
    path('post/<str:slug>/', GetPost.as_view(), name = 'post'),
    path('posts/', GetAllPost.as_view(), name = 'posts'),
    path('', Home.as_view(), name = 'home'),
    ]