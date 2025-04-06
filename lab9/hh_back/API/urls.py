from django.contrib import admin
from django.urls import path, include

from API.views import *

urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:pk>/', get_company),
    path('vacancies/', get_vacancies),
    path('vacancies/<int:pk>/', get_vacancy),
    path('companies/<int:pk>/vacancies/',get_vacancies_from_company),

]
