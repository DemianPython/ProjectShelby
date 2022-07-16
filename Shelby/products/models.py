from asyncio.windows_events import NULL
from email.policy import default
from pickle import TRUE
from tkinter import N
from tokenize import blank_re
from unicodedata import category
from django.db import models
from django.forms import CharField


# Create your models here.

class Products(models.Model):
    Nombre = models.CharField(max_length=50)
    Precio = models.FloatField()
    Categoria = models.CharField(max_length=100, default= NULL)
    SKU = models.IntegerField()
    Cantidad = models.IntegerField(default=0)

