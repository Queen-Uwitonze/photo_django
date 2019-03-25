from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views 
from django.contrib.auth.views import logout

urlpatterns=[
   
    url(r'^$', views.images_of_today,name='galleryToday'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^logout/', views.logout, {"next_page": '/'}), 
    url(r'^image/(\d+)', views.single_images,name ='images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)