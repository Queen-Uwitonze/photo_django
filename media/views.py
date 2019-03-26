from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import Profile ,Photo
from .forms import NewProfileForm, GalleryLetterForm,PhotoForm

@login_required(login_url='/accounts/login/')
def photos(request):
    
    if request.method == 'POST':
        form = GalleryLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = GalleryLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('photos')
    else:
        form = GalleryLetterForm()
    return render(request, 'all_gallery/today-gallery.html',{"letterForm":form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect(galleryToday)

    else:
        form = NewProfileForm()
    return render(request, 'all_gallery/new-profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get()
    profile = Profile.objects.get(user = user)
   
    return render(request,'all_gallery/profile.html',{"profile":profile,"user":user})

def photo(request):
    current_user = request.user
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()

    else:
        form = PhotosForm()
    return render(request, 'image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def photoes(request,image_id):
    photo =Photo.objects.get(id = image_id)
    return render(request,"info.html", {"image":image})