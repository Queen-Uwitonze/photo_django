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

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

class Photos(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'gramys/')
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =200)
   
    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

    @classmethod
    def get_photoes(cls):
        images = cls.objects.all()
        return images    

class GalleryLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


