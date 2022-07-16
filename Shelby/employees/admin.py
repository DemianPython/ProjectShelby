from django.contrib import admin

from .models import Employeer, Salary

# Register your models here.

admin.site.register(Employeer)
admin.site.register(Salary)