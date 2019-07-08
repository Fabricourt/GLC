from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_1 = models.CharField(max_length=200, unique=True, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=200, unique=True, blank=True, null=True)
    facebook = models.CharField(max_length=200, unique=True, blank=True, null=True)
    twitter = models.CharField(max_length=200, unique=True, blank=True, null=True)
    linkedin = models.CharField(max_length=200, unique=True, blank=True, null=True)
    address = models.CharField(max_length=200, unique=True, blank=True, null=True)
    country = models.CharField(max_length=200,  blank=True, null=True)
    county = models.CharField(max_length=200,  blank=True, null=True)
    state = models.CharField(max_length=200,  blank=True, null=True)
    town = county = models.CharField(max_length=200,  blank=True, null=True)
    county = models.CharField(max_length=200,  blank=True, null=True)
    bio = RichTextField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 130 or img.width > 130:
            output_size = (130, 130)
            img.thumbnail(output_size)
            img.save(self.image.path)