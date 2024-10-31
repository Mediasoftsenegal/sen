
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from sites import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sites.urls')),
    path('ckeditor',include('ckeditor_uploader.urls'))
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)