from PIL import Image
from django import forms
from django.core.files import File
from .models import Photo

class GalleryLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('description', 'document', )