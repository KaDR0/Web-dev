from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Company
from .models import Vacancy
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class GetVacancies(APIView):
    def get(self, request):
        queryset = Vacancy.objects.all()
        serializer = VacanciesSerializer(queryset, many=True)
        return Response(serializer.data)


class GetCompanies(APIView):
    def get(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


# class based CRUD view
class CompanyViews(APIView):
    def get(self, request, pk=None):
        queryset = Company.objects.get(id=pk)
        serializer = CompanySerializer(queryset)
        return Response(serializer.data)

    def post(self, request, pk=None):
        pass


# function based CRUD view
def vacancy_views(request, pk=None):
    if request.method == 'GET':
        queryset = Vacancy.objects.get(id=pk)
        serializer = VacanciesSerializer(queryset)
        return JsonResponse(serializer.data)


class VacanciesByCompanyView(APIView):
    def get(self, request, pk=None):
        queryset = Vacancy.objects.filter(company_id=pk)
        serializer = VacanciesSerializer(queryset, many=True)
        return Response(serializer.data)



def get_vacancies_top_ten(request):
    vacancies = Vacancy.objects.order_by('salary')[:10]
    json_data = [vac.to_json() for vac in vacancies]
    return JsonResponse(json_data, safe=False)
