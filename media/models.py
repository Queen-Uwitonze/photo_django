from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to='profiles/', blank=True)
    bio = models.TextField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)



class GalleryLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


