from django.shortcuts import render, redirect
from .models import Salary,Employeer
from .forms import Salary_form, Employeer_form
# Create your views here.

def employees(request):
    return render(request, 'menu_employees.html', context={})

def create_salary(request):
    if request.method == 'GET':
        form_salary = Salary_form()
        context = {'form_salary':form_salary}
        return render(request, 'create_salary.html', context=context)
    else:
        form = Salary_form(request.POST)
        if form.is_valid():
            new_salary = Salary.objects.create(
                Empleado = form.cleaned_data['Empleado'],
                Sueldo = form.cleaned_data['Sueldo'],
                Comisiones = form.cleaned_data['Comisiones'],
                Mes = form.cleaned_data['Mes'],
                Año = form.cleaned_data['Año'],
                Total = form.cleaned_data['Total'],
            )
            context ={'new_salary':new_salary}
        return redirect('/see-salary')

def see_salary(request):
    salary = Salary.objects.all()
    context = {'salary':salary}
    return render(request, 'see_salary.html', context = context)

def create_employeer(request):
    if request.method == 'GET':
        form_employeer = Employeer_form()
        context = {'form_employeer':form_employeer}
        return render(request, 'create_employeer.html', context=context)
    else:
        form = Employeer_form(request.POST)
        if form.is_valid():
            new_employeer = Employeer.objects.create(
                Nombre = form.cleaned_data['Nombre'],
                Cargo = form.cleaned_data['Cargo'],
                Inicio_laboral = form.cleaned_data['Inicio_laboral'],
                Sueldo_mensual = form.cleaned_data['Sueldo_mensual'],
                Cuenta_corriente = form.cleaned_data['Cuenta_corriente'],
            )
            context ={'new_employeer':new_employeer}
        return redirect('/see-employeer')

def see_employeer(request):
    employeer = Employeer.objects.all()
    context = {'employeer':employeer}
    return render(request, 'see_employeer.html', context = context)