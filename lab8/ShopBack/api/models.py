from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"name:{self.name}, price:{self.price}, count:{self.count}, is_active:{self.is_active},description:{self.description}"

    def to_json(self):
        return dict(name=self.name,
                    price=self.price,
                    description=self.description,
                    count=self.count,
                    is_active=self.is_active)
