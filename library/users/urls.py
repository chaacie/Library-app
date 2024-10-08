from django.contrib import admin
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.sign_up, name='sign_up')
]