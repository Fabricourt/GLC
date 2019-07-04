from django.db import models
from django.utils import timezone
from datetime import datetime
from accounts .models import User
from ckeditor.fields import RichTextField
from PIL import Image

class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    event_pic = models.ImageField(upload_to='events/%Y/%m/%d/', blank=False, null=True)
    event_detail = RichTextField(blank=False, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    event_contact_person = models.CharField(max_length=200, unique=True, blank=True, null=True)
    event_contact = models.CharField(max_length=200, unique=True, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.event_name
    
    def dayevent(self):
        return self.event_date.strftime('%d')
    
    def monthevent(self):
        return self.event_date.strftime('%b')

    def yearevent(self):
        return self.event_date.strftime('%Y')
    
    def startevent(self):
        return self.event_date.strftime('%I.%M-%p')

    def stopevent(self):
        return self.end_date.strftime('%I.%M-%p')

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


