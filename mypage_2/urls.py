from django.urls import path
from mypage_2.views import info_views

#127.0.0.1:8000/info/
urlpatterns = [
    path('', info_views),

]