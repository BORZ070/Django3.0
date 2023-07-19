from django.shortcuts import render
from mypage.models import Book

def year_views(request):
    books = Book.objects.all()
    return render(request, 'index_year.html', {'books': books})
