from django.db import models
from django.utils import timezone
from django.urls import reverse 
from django.contrib.auth.models import User  
from ckeditor.fields import RichTextField



class Team(models. Model):
    team = models.ForeignKey(User, on_delete=models.CASCADE)
    team_header = models.ImageField(upload_to='team_header/', blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.phone
