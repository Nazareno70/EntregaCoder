from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from Appcoder.models import Familia
from django.template import loader

def crear_profesor(request):
    template= loader.get_template("template.html")

    flia=Familia (nombre="Juan Carlos", apellido="Martin", email="juan@gmail.com", profesion="Abogado")
    flia_2=Familia (nombre="Belen", apellido="Frati", email="belen_frati@gmail.com", profesion="Arquitecta")
    flia_3=Familia (nombre="Nazareno", apellido="Martincevich", email="nazareno@gmail.com", profesion="Economista")

    dict_de_contexto={
        "flia_1": flia,
        "flia_2": flia_2,
        "flia_3": flia_3,
    
    }

    res= template.render(dict_de_contexto)

    return HttpResponse (res)
