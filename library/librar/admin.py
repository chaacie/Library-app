from django.contrib import admin
from .models import Book, BorrowedBook
from users.models import CustomUser

# Register your models here.
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(CustomUser)