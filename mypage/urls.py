from django.urls import path
from mypage.views import start_views

#127.0.0.1:8000/
urlpatterns = [
    path('', start_views),

]
