from django.shortcuts import render
from mypage.models import Book

def start_views(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def detail_views(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'detail.html', {'book': book})


