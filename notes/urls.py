# -*- coding: utf-8 -*-

from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('hello/', views.hello, name='notes'),
]
