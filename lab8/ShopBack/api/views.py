import product
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, JsonResponse

from api.models import Category

from api.models import Product


def get_categories(request, c_id=None):
    if c_id is None:
        categories = Category.objects.all()
        categories_json = [cat.to_json() for cat in categories]
        return JsonResponse(categories_json, safe=False)
    else:
        try:
            category = Category.objects.get(id=c_id)
            return JsonResponse(category.to_json(), safe=False)
        except Category.DoesNotExist as e:
            return JsonResponse({
                'error': str(e)
            })


def get_products(request, p_id=None):
    if p_id is None:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    else:
        try:
            product = Product.objects.get(id=p_id)
            return JsonResponse(product.to_json(), safe=False)
        except Product.DoesNotExist as e:
            return JsonResponse({
                'error': str(e)
            })


def get_products_by_category(request, pk=None):
    try:
        category = Category.objects.get(id=pk)
        products = Product.objects.filter(categories=category)
        products_json = [prod.to_json() for prod in products]

        return JsonResponse(products_json, safe=False)

    except Category.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)})
