from django.contrib import admin
from django.urls import path

from upload.views import image_upload

urlpatterns = [
    path('', image_upload, name='upload'),
    path('admin/', admin.site.urls),
]
