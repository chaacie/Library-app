# api/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from librar.models import Book, BorrowedBook
from .serializers import BookSerializer, BorrowedBookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if BorrowedBook.objects.filter(book=book, user=request.user, returned__isnull=True).exists():
            return Response({'detail': 'Вы уже взяли эту книгу.'}, status=status.HTTP_400_BAD_REQUEST)

        BorrowedBook.objects.create(book=book, user=request.user)
        return Response({'detail': 'Книга успешно взята.'}, status=status.HTTP_200_OK)

class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        borrowed_book = get_object_or_404(BorrowedBook, book=book, user=request.user, returned__isnull=True)
        borrowed_book.returned_at = timezone.now()
        borrowed_book.save()
        return Response({'detail': 'Книга успешно возвращена.'}, status=status.HTTP_200_OK)

class MyBooksListView(generics.ListAPIView):
    serializer_class = BorrowedBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowedBook.objects.filter(user=self.request.user, returned__isnull=True)
