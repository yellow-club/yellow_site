from django.urls import path

from .views import *

urlpatterns = [
    path('event/<str:slug>/', GetEvent.as_view(), name = 'event'),
    path('', GetAllEvents.as_view(), name = 'events'),
    ]