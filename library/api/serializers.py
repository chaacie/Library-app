from rest_framework import serializers
from librar.models import Book, BorrowedBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']


class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BorrowedBook
        fields = ['book', 'borrowed_at']