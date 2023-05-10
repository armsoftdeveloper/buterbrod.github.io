from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django_translation_flags.urls')),
]

#--------------------------------------------- Static Condition For Debug Type  ---------------------------------------------#

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#--------------------------------------------- Handlers  ---------------------------------------------#

handler404 = pageNotFound