from django.shortcuts import render
from .models import Book  # Импорт модели

def book_list(request):
    books = Book.objects.all()  # Получаем все книги
    return render(request, 'books/book_list.html', {'books': books})

def unavailable_books(request):
    return render(request, 'books/unavailable_books.html')


