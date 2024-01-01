from rest_framework import serializers
from .models import Author, Genre, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()
    genres = GenreSerializer()
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {'book_Main_img': {'required': False}}