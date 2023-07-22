from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mypage.views import start_views
from mypage_2.views import info_views
from mypage_year.views import year_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mypage.urls', namespace='mypage')),
    path('info', include('mypage_2.urls', namespace='mypage_2')),
    path('year', include('mypage_year.urls', namespace='mypage_year'))


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    