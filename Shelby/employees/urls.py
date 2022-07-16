from django.contrib import admin
from django.urls import path
from .views import create_employeer, create_salary, employees, see_employeer,see_salary

urlpatterns = [
    path('create-salary/', create_salary , name = 'create-salary'),
    path('see-salary/', see_salary , name = 'see-salary'),
    path('create-employeer/', create_employeer , name = 'create-employeer'),
    path('see-employeer/', see_employeer , name = 'see-employeer'),
    path('employees/', employees, name = 'employees'),
]

