from django import forms
from .models import Products
class Products_form(forms.ModelForm):
    class Meta:
        model = Products
        fields=[
        "Nombre",
        "Precio",
        "Categoria",
        "Marca",
        "SKU",
        "Cantidad",
        
        ]
   