# Generated by Django 4.2.3 on 2023-07-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_book_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover'),
        ),
    ]
