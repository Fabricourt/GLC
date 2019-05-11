from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='gallerys'),
    path('<int:gallery_id>', views.gallery_detail, name='gallery'),
    
]