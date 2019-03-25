from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib.auth.views import logout

urlpatterns=[
   
    url(r'^$', views.photos,name='galleryToday'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)