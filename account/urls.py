# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    # предыдущий url-адрес входа
    # path('login/', views.user_login, name='login'),
    # url-адреса входа и выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
