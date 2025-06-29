from django.shortcuts import render, HttpResponse
from .models import Alumnas

# Create your views here.
def principal (request):
    return render(request, "inicio/principal.html")

def contacto (request):
    return render(request, "inicio/contacto.html")

def formulario (request):
    return render(request, "inicio/formulario.html")

def ejemplo (request):
    return render(request, "inicio/ejemplo.html")

def registros (request):
    #Recuperamos todos los objetos de la tabla alumnas
    alumnas=Alumnas.objects.all()
    return render(request, "registros/principal.html", {'alumnas':alumnas})