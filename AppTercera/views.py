from django.shortcuts import render
from django.http import HttpResponse
from AppTercera.models import *
# Create your views here.


def inicio(request):

    return render(request, "inicio.html")

# En estas vistas se muestra

def MostrarEmpleados(request):

    return render(request, "MostrarEmpleados.html")

def MostrarClientes(request):

    return render(request, "MostrarClientes.html")

def MostrarVentas(request):

    return render(request, "MostrarVentas.html")

# En estas vistas se carga

def CargarEmpleados(request):

    return render(request, "CargarEmpleados.html")

def CargarClientes(request):

    return render(request, "CargarClientes.html")

def CargarVentas(request):

    return render(request, "CargarVentas.html")

# en esta vista se busca, luego con las funcionalidades definiré a donde busca

def Buscar(request):

    return render(request, "Buscar.html")