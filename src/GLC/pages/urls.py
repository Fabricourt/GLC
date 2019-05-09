from django.urls import path
from django.shortcuts import redirect
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),   
] 