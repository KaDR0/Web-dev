from rest_framework import serializers

from API.models import Company


# serializer based on serializer.Serializer
class VacanciesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    salary = serializers.FloatField()
    company = serializers.CharField(source='company.name', max_length=200)


# serializer based on serializer.ModelSerializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
