from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to='profiles/', blank=True)
    bio = models.TextField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

class Photo(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'profiles/')
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =60)
    # comments = models.ForeignKey(User,on_delete=models.CASCADE)
    # likes = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()
    
    def delete_photo(self):
        self.delete()

    @classmethod
    def get_photos(cls,id):
        photo = Photo.objects.all()
        return photo   

class GalleryLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Comments(models.Model):
    comments = models.CharField(max_length = 300)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE,related_name='photo')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
   
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.objects.all()
        return comments

class Likes(models.Model):
    likes= models.IntegerField(default=0)
    photo= models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes

