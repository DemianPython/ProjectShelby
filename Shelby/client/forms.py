from dataclasses import fields
from .models import Clients
from django import forms

class Clients_form(forms.ModelForm):
    class Meta:
        model = Clients
        fields=[
            "Nombre_del_cliente",
            "Nombre_del_local",
            "Localidad",
            "Direccion_del_local",
            "Cuenta_corriente",

        ]