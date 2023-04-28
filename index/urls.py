# -*- coding: utf-8 -*-
from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/<category_id>/', views.category, name='category'),
    # path('category/', views.category, name='category'),
    path('add-note/', views.add_note, name='add_note'),
    path('edit-note/<int:id>/', views.edit_note, name='edit_note'),
    path('del-note/<int:id>/delete', views.delete_notes, name='delete_notes'),
]
