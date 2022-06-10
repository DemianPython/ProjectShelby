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
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(max_length=100, default= NULL)
    SKU = models.IntegerField()
    quantity = models.IntegerField(default=0)

