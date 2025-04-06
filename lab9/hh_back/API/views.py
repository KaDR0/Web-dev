from django.shortcuts import render

from .models import Company
from .models import Vacancy
from django.http.response import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json


# Create your views here.


def get_companies(request):
    companies = Company.objects.all()
    json_data = [comp.to_json() for comp in companies]
    return JsonResponse(json_data, safe=False)


def get_company(request, pk=None):
    try:
        company = Company.objects.get(id=pk)
        return JsonResponse(company.to_json())
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


def get_vacancies(request):
    vacancies = Vacancy.objects.all().values()
    # return JsonResponse(serialize('json', vacancies), safe=False)
    data = [vac.to_jsonn() for vac in vacancies]
    return JsonResponse(data, safe=False)


def get_vacancy(request, pk=None):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(serialize('json', [vacancy]), safe=False)


def get_vacancies_from_company(request, pk=None):
    vacancies = Vacancy.objects.filter(company_id=pk)
    return JsonResponse(serialize('json', vacancies), safe=False)
