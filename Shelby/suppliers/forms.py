from operator import contains
from django import forms

from .models import Suppliers, OrderProducts

class OrderProducts_form(forms.ModelForm):
    class Meta:
        model=OrderProducts
        fields=[
        "Empresa",
        "Lista_de_productos",
        "Fecha_de_pedido",
        "Fecha_de_entrega",
        "Total",
        ]
    
    

class Suppliers_form(forms.ModelForm):
     class Meta:
        model=Suppliers
        fields=[
        "Nombre", "Telefono_de_contacto"]
    