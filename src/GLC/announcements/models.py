from django.db import models
from django.utils import timezone
from accounts .models import User
from ckeditor.fields import RichTextField
#from PIL import Image

class Announcement(models.Model):
    title = models.CharField(max_length=200, unique=True)
    announcement = RichTextField(blank=False, null=True)
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
    