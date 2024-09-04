from django.urls import path
from .views import BookListView, BorrowBookView, ReturnBookView, MyBooksListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('books/', BookListView.as_view(), name='api_books'),
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='api_borrow_book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='api_return_book'),
    path('my-books/', MyBooksListView.as_view(), name='api_my_books'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
