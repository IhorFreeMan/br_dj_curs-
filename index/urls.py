# -*- coding: utf-8 -*-

from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/<category_id>/', views.category, name='category'),
    # path('category/', views.category, name='category'),
]
