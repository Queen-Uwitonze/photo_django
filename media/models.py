from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class GalleryLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


