from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
from tokenize import Triple, blank_re
from django.db import models
from django.forms import CharField

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    description = models.CharField(max_length=200)
    SKU = models.IntegerField()
    image = models.ImageField( null = True)