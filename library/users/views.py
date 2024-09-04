from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalog')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('users:login')


def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = CreateUserForm()

    return render(request, 'users/sign_up.html', {'form':form})