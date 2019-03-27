# from PIL import Photo
from django import forms
from django.core.files import File
from .models import Profile,Photo,Comments,Likes

class GalleryLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user','profile']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []

class LikeForm(forms.ModelForm):
    class Meta:
        model = Likes
        exclude = ['user','image']