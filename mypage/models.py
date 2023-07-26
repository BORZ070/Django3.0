from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    info = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='book_cover', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='book_cover', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='book_cover', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='book_cover', blank=True, null=True)


    def __str__(self):
        return f'{self.id} // {self.name}'

