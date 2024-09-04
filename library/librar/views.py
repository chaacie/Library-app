from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Book, BorrowedBook
from users.forms import UpdateUserInfo
from django.contrib.auth.decorators import login_required
from datetime import timezone
from django.utils import timezone
# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login.html')


def catalog(request):
    borrowed_books = BorrowedBook.objects.filter(returned__isnull=True).values_list('book_id', flat=True)
    available_books = Book.objects.exclude(id__in=borrowed_books).order_by('title')

    return render(request, 'catalog.html', {'books': available_books})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    BorrowedBook.objects.create(book=book, user=request.user)
    return redirect('catalog')


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    borrowed_books = BorrowedBook.objects.filter(book=book, user=request.user, returned__isnull=True)

    if borrowed_books.exists():
        for borrowed_book in borrowed_books:
            borrowed_book.returned = timezone.now()
            borrowed_book.save()

    return redirect('catalog')


@login_required
def my_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user, returned__isnull=True).order_by('book__title')
    return render(request, 'my_books.html', {'borrowed_books': borrowed_books})



@login_required
def librian_page(request):
    if not request.user.is_librian:
        return HttpResponse('Вы не имеете прав доступа к этой странице')
    overdue_books = BorrowedBook.objects.filter(returned__isnull=True).select_related('user', 'book')
    overdue_books = overdue_books.order_by('-borrowed_at')


    return render(request, 'librian_page.html', {'overdue_books': overdue_books})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление после успешного обновления профиля
    else:
        form = UpdateUserInfo(instance=request.user)

    return render(request, 'profile.html', {'form': form})




