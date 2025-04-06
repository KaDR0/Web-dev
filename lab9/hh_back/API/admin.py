from django.contrib import admin
from API.models import Company, Vacancy


# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'city')
    search_fields = ('name',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'salary', 'company')
    search_fields = ('name',)
