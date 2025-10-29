from django.shortcuts import render
from django.http import HttpResponse as res

# Create your views here.

# Hola esto es una prueba de textos

def hello(req):
    return res("<h1>Hola Mundo</h1>")