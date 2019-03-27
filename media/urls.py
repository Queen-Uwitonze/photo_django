from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib.auth.views import logout

urlpatterns=[
    
    url(r'^$', views.index,name='home'),
    url(r'^profile/', views.new_profile, name='profile'),
    url(r'^new/profile', views.profile, name='new-profile'),
    url(r'^image/', views.photos, name='image'),

    url(r'^photo/(\d+)', views.images, name='details'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)