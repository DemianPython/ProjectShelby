from multiprocessing.sharedctypes import Value
from django.db import models

class Employeer(models.Model):
    Nombre = models.CharField(max_length=50)
    Cargo =  models.CharField(max_length=100)
    Inicio_laboral = models.CharField(max_length=100)
    Sueldo_mensual = models.FloatField(max_length=50)
    Cuenta_corriente = models.FloatField(max_length=50, default=0)
    
    def __str__(self):
        return self.Nombre

class Salary(models.Model):
    Empleado = models.ForeignKey('Employeer', on_delete=models.CASCADE)
    Sueldo = models.FloatField()
    Comisiones = models.FloatField(null=Value)
    Mes = models.CharField(max_length=50)
    Año = models.IntegerField()
    Total = models.FloatField(null=Value)
    
    

