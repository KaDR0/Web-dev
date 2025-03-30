from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # Название книги
    author = models.CharField(max_length=255)  # Автор книги
    copies_available = models.IntegerField(default=0)  # Количество доступных копий
    loan_records = models.JSONField(default=list)  # Список дат выдачи книги

    def is_available(self):
        """Проверяет, есть ли доступные копии книги."""
        return self.copies_available > 0

    def get_most_recent_loan(self):
        """Возвращает последнюю дату выдачи книги."""
        if self.loan_records:
            return max(self.loan_records)  # Находит самую позднюю дату
        return None

    def __str__(self):
        return self.title
