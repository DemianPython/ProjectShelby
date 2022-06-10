from django.contrib import admin
from django.urls import path
from .views import create_products, menu_products, see_products

urlpatterns = [
    path('products/', menu_products , name = 'products'),
    path('see-products/', see_products , name = 'see-products'),
    path('create-products/', create_products , name = 'create-products'),
]

