from django.contrib import admin

from .models import Suppliers, OrderProducts

# Register your models here.
admin.site.register(Suppliers)
admin.site.register(OrderProducts)