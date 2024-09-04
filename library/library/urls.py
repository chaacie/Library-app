"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from librar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalog, name='catalog'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('users/', include('users.urls', namespace='users')),
    path('my_books/', views.my_books, name='my_books'),
    path('librian_page/', views.librian_page, name='librian_page'),
    path('api/', include('api.urls')),
    path('profile/', views.profile, name='profile')
]
