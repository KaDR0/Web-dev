from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"ID:{self.id}, name: {self.name}, description: {self.description}, city: {self.city}, address:{self.address}"

    class Meta:
        verbose_name_plural = "Companies"

    def to_json(self):
        return dict(
            name=self.name,
            description=self.description,
            city=self.city,
            address=self.address
        )


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return f"ID:{self.id}, name:{self.name}, description: {self.description}, salary: {self.salary}, company: {self.company}"

    class Meta:
        verbose_name_plural = "Vacancies"

    def to_json(self):
        return (
            f"name: {self.name}",
            f"description={self.description}",
            f"salary={self.salary}",
            f"company={self.company}"

        )
