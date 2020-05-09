from rest_framework import serializers

from api.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", 'author')


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class AuthorBooksSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Author
        fields = ('name', 'books',)
