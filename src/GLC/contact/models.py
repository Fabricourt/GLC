from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.ForeignKey(User, on_delete= models.CASCADE,blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)

    def _str (self):
        return f'{self.name} {self.email} {self.phone}'