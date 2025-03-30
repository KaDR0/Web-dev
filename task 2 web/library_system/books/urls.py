from django.urls import path
from .views import book_list, unavailable_books

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/unavailable-books/', unavailable_books, name='unavailable_books'),
]