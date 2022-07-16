from django import forms
from .models import Employeer, Salary

class Salary_form(forms.ModelForm):
    class Meta:
        model = Salary
        fields=[
            "Empleado",
            "Sueldo",
            "Comisiones",
            "Mes",
            "Año",
            "Total"
            ]

class Employeer_form(forms.ModelForm):
    class Meta:
        model = Employeer
        fields=[
            "Nombre",
            "Cargo",
            "Inicio_laboral",
            "Sueldo_mensual",
            "Cuenta_corriente",
            ]