from django.contrib import admin
from django.urls import path, include
import urllib2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls'))
]
