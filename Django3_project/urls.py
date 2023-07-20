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
