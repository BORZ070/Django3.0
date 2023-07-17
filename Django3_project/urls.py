from django.contrib import admin
from django.urls import path

from mypage.views import start_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_views)
]
