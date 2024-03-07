
from django.contrib import admin
from django.urls import path
from AppTercera.views import *
urlpatterns = [
    path("", inicio, name="Home"),
    path("CargarClientes", CargarClientes, name="CargarClientes"),
    path("CargarEmpleados", CargarEmpleados, name="CargarEmpleados"),
    path("CargarVentas", CargarVentas, name="CargarVentas"),
    path("MostrarVentas", MostrarVentas, name="MostrarVentas"),
    path("MostrarEmpleados", MostrarEmpleados, name="MostrarEmpleados"),
    path("MostrarClientes", MostrarClientes, name="MostrarClientes"),
    path("Buscar", Buscar, name="Buscar"),
   
   
]

