from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import Profile 
from .forms import NewProfileForm, GalleryLetterForm

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
def new_Profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('galleryToday')

    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    profile = Profile.objects.all()
    return render(request, 'profile.html', locals())

