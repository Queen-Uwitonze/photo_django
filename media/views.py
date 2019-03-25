from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt

from django.contrib.auth.decorators import login_required
from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email


# Create your views here.
    
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

def model_form_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
    })
