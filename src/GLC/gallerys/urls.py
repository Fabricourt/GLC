from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='photos'),
    path('<int:photo_id>', views.photo_detail, name='photo'),
    
]