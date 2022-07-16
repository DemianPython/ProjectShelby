from django.contrib import admin
from django.urls import path
from .views import  create_suppliers, see_suppliers, suppliers, create_Order_Products, see_OrderProducts


urlpatterns = [
    path('suppliers/', suppliers, name = 'suppliers'),
    path('create-suppliers/', create_suppliers , name = 'create-suppliers'),
    path('see-suppliers/', see_suppliers , name = 'see-suppliers'),
    path('create-orden-products/', create_Order_Products , name = 'create-orden-products'),
    path('see-order/', see_OrderProducts , name = 'see-order'),



]
