from django.db import models
from django.utils import timezone


# Create your models here.
class Topbar(models.Model):
    title = models.CharField(max_length=100)
    statement = models.CharField(max_length=100, blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
class Head(models.Model):
    title = models.CharField(max_length=100)
    home_header = models.ImageField(upload_to='home_header/', blank=True, null=True)
    logo_short_name = models.CharField(max_length=20, blank=True, null=True)
    motivational_statement = models.CharField(max_length=20, blank=True, null=True) 
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Footer(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title