from django.db import models

# Create your models here.

class Clients(models.Model):
    Nombre_del_cliente = models.CharField(max_length=50)
    Nombre_del_local = models.CharField(max_length=50)
    Localidad = models.CharField(max_length=50)
    Direccion_del_local = models.CharField(max_length=50)
    Cuenta_corriente = models.FloatField()