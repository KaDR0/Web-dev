from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Добавляем импорт

urlpatterns = [
    path('', lambda request: redirect('book_list')),  # Перенаправление на список книг
    path('books/', include('books.urls')),  # Подключение маршрутов из books
    path('admin/', admin.site.urls),
]