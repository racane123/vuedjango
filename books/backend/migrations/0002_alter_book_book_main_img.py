# Generated by Django 5.0 on 2023-12-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_Main_img',
            field=models.ImageField(upload_to='books/'),
        ),
    ]
