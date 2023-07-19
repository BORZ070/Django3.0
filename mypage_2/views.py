from django.shortcuts import render
from mypage.models import Book


def info_views(request):
    books = Book.objects.all()
    return render(request, 'index_2.html', {'books': books})

