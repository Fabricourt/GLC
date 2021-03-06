"""GLC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include # url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as account_views
from contact import views as contact_views



urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('team/', include('team.urls')),
    path('gallerys/', include('gallerys.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', account_views.profile, name='profile'),
    path('contact/', contact_views.contact, name='contact'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
