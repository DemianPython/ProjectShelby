from asyncio.windows_events import NULL
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Products(models.Model):
    Nombre = models.CharField(max_length=50)
    Precio = models.FloatField()
    Categoria = models.CharField(max_length=100, default= NULL)
    Marca = models.CharField(max_length=100, null=True)
    SKU = models.IntegerField()
    Cantidad = models.IntegerField(default=0)

