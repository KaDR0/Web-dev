from django.contrib import admin
from django.urls import path

from api.views import get_categories, get_products, get_products_by_category

urlpatterns = [
    path('categories/<int:c_id>/', get_categories),
    path('categories/', get_categories),
    path('products/', get_products),
    path('products/<int:p_id>', get_products),
    path('categories/<int:pk>/products/', get_products_by_category),

]
