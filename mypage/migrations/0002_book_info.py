# Generated by Django 4.2.3 on 2023-07-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
