from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


#URLs para rastreo e indexacion
url_SEO = [
    # Bots.txt
]


#URLs para servicios
url_API = [

]


#URLs propias del sitio
url_BASE = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.graphics.urls')),
    path('', include('apps.sensors.urls')),
    path('', include('apps.lectures.urls')),
]


#URLs totales
urlpatterns = url_SEO + url_BASE

#Habilitación ficheros estaticos DEV
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Vistas Errores


# Nombre Admin
admin.site.site_title = "Panel de control"
admin.site.site_header = "ConvictionApp"
admin.site.index_title = "Panel de control | Conviction | App"