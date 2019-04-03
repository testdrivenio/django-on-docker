from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload

urlpatterns = [
    path('', image_upload, name='upload'),
    path('admin/', admin.site.urls),
]

# to allow static in development mode. it could be removed when run via nginx
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
