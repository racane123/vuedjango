from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    birth_date = models.DateField()

class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

class Book(models.Model):
    book_Main_img = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=255)
    summary = models.TextField()
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    published_date = models.DateField()