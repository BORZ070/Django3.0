from django.urls import path
from mypage.views import start_views, detail_views

app_name = 'mypage'

#127.0.0.1:8000/
urlpatterns = [
    path('', start_views, name='indexpage'),
    path('book/<int:pk>', detail_views, name='detailpage')
]
