from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title  = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class header(models.Model):
    title = models.CharField(max_length=100)
    header = models.ImageField(upload_to='header/', blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class category(models.Model):
    title  = models.CharField(max_length=120)
    image1   = models.ImageField(upload_to='image1/', blank=True, null=True)
    statements = models.CharField(max_length=200, null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title