from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import Profile ,Photo
from .forms import NewProfileForm, GalleryLetterForm,PhotoForm,CommentsForm

@login_required(login_url='/accounts/login/')
def index(request):
    photo = Photo.objects.all()
    profile = Profile.objects.all()
    return render(request, 'home.html',{"photo":photo,"profile":profile})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect("home")

    else:
        form = NewProfileForm()
    return render(request, 'all_gallery/new-profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get()
    profile = Profile.objects.get(user = user)
   
    return render(request,'all_gallery/profile.html',{"profile":profile,"user":user})

@login_required(login_url='/accounts/login/')
def photos(request):
    current_user = request.user
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.profile = current_user
            photo.save()

        return redirect("home")

    else:
        form = PhotoForm()
    return render(request, 'images.html', {"form": form})

@login_required(login_url='/accounts/login/')
def photo(request):
    current_user = request.user
    
    return render(request,"all_gallery/today-gallery.html")


def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()

            return redirect("home")

    else:
        form = CommentsForm()
    return render(request, 'comment.html', {"form": form})

@login_required(login_url='/accounts/login/')
def com(request,image_id):
    photo = Photo.objects.get(id = image_id)
    comments = Comments.objects.filter(image = image.id).all() 
    likes = Like.objects.filter(image = image.id).all() 