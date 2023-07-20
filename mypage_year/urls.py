from django.urls import path
from mypage_year.views import year_views

app_name = 'mypage_year'

#127.0.0.1:8000/info/
urlpatterns = [
    path('', year_views, name='yearpage'),

]