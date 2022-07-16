from dataclasses import Field
from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.
class OrderProducts(models.Model):
    Empresa  = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    Lista_de_productos = models.TextField(max_length=10000)
    Fecha_de_pedido = models.CharField(max_length=8)
    Fecha_de_entrega = models.CharField(max_length=8)
    Total = models.FloatField()

class Suppliers(models.Model):
    Nombre = models.CharField(max_length=100)
    Telefono_de_contacto = models.IntegerField(null = True)
    def __str__(self):
        return self.Nombre
    