from django.urls import path
from mypage_year.views import year_views

#127.0.0.1:8000/info/
urlpatterns = [
    path('', year_views),

]