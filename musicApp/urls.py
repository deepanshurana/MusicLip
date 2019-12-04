from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls.static import static
urlpatterns = [
               re_path(r'^admin/', admin.site.urls),
               # re_path(r'^music/', include('music.urls', namespace='music')),
               re_path(r'^', include('music.urls', namespace='music')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
