from asyncio.windows_events import NULL
from unicodedata import category
from django import forms

class Products_form(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    category = forms.CharField(max_length=100)
    SKU = forms.IntegerField()
    quantity = forms.IntegerField()