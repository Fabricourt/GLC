from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class gallery(models.Model):
    title  = models.CharField(max_length=120)
    picture   = models.ImageField(upload_to='picture/', blank=True, null=True)
    description = RichTextField(null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title