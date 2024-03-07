from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fingreso = models.DateField() 
    edJornada_Extendida = models.BooleanField()

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.nombre} --- {self.categoria}"

class Ventas(models.Model):
    nro_factura = models.CharField(max_length=30)
    denominacion = models.CharField(max_length=50)
    fecha = models.DateField()
