from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from .models import Images,Category,Location
from django.contrib.auth.decorators import login_required
from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email


# Create your views here.

# def convert_dates(dates):
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
    # return day
    
@login_required(login_url='/accounts/login/')
def images_of_today(request):
    # gallery = Images.objects.all()
    # date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    
    if request.method == 'POST':
        form = GalleryLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = GalleryLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('images_of_day')
    else:
        form = GalleryLetterForm()
    return render(request, 'all_gallery/today-gallery.html',{'gallery':gallery},{"letterForm":form})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        categories = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_gallery/search.html',{"message":message,"categories": categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_gallery/search.html',{"message":message})      

def single_images(request,image_id):
    images = Images.objects.get(id=image_id)
    return render(request,"all_gallery/single_image.html", {"images":images})

