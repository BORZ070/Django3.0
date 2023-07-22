from django.contrib import admin
from mypage.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    list_display_links = ('id', 'name', 'author')

admin.site.register(Book, BookAdmin)
