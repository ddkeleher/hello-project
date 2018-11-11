from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
