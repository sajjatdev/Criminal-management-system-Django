from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from view import urls as VIEWURl


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(VIEWURl), name="View")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
