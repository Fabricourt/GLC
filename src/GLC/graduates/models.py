from django.db import models
from django.utils import timezone
from accounts .models import User
from ckeditor.fields import RichTextField
from PIL import Image




class Graduate(models.Model):
  graduates = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200, blank=True, null=True)
  description = RichTextField(blank=True, null=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  Date_of_arrival = models.DateTimeField(default=timezone.now)
  Date_of_graduation = models.DateTimeField(default=timezone.now)
  timestamp = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.title