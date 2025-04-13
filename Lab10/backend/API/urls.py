from django.contrib import admin
from django.urls import path, include

from API.views import *

urlpatterns = [
    path('companies/', GetCompanies.as_view()),
    path('companies/<int:pk>/', CompanyViews.as_view()),
    path('vacancies/', GetVacancies.as_view()),
    path('vacancies/<int:pk>/', vacancy_views),
    path('companies/<int:pk>/vacancies/',VacanciesByCompanyView.as_view()),
    path('vacancies/top_ten/', get_vacancies_top_ten)
]
