from django.urls import path
from django.shortcuts import redirect
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about', views.about, name='about'),
    path('mobile', views.mobile, name='mobile'), 
    path('tablet', views.tablet, name='tablet'),
    path('laptop', views.laptop, name='laptop')
] 