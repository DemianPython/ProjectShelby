from django.contrib import admin
from django.urls import path
from .views import Delete_products, Create_products, menu_products, see_products, Detail_products, Update_products

urlpatterns = [
    path('products/', menu_products , name = 'products'),
    path('see-products/', see_products , name = 'see-products'),
    path('create-products/', Create_products.as_view() , name = 'create-products'),
    path('delete-products/<int:pk>/', Delete_products.as_view(), name = 'delete-products'),
    path('detail-products/<int:pk>/', Detail_products.as_view(), name = 'detail-products'),
    path('update-products/<int:pk>/', Update_products.as_view(), name = 'update-products')
]

