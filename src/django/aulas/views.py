from django.shortcuts import render
from django.http import HttpResponse as res
from datetime import date as dt
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def hello(req):
    return res("<h1>Hola Mundo</h1>")


def bye(req):
    return res("<h1>Hasta luego</h1>")


def edad(req, anios, futuro):
    anio_actual = dt.today().year
    incremento = futuro - anio_actual
    cumplira = anios + incremento
    return res("en el anio %d cumpliras %d anios" % (futuro, cumplira))


def primer_plantila(req):
    plantilla = """
    
    """

    tpl = Template(plantilla)
    ctx = Context({"nombre":"Alberto Carmona"})
    mensaje = tpl.render(ctx)

    return res(mensaje)


def segunda_plantilla(req):
    tpl = get_template("segunda_pantilla.html")
    ctx = {
        "nombre": "Santiago Carmona",
        "fecha_actual":dt.today(),
        'titulo':'mi sitio web en django',
        }
    mensaje = tpl.render(ctx)

    return res(mensaje)

def tercer_plantilla(req):

    ctx = {
        "nombre": "Santiago Carmona",
        "fecha_actual": dt.today(),
        "titulo": "mi sitio web en django",
    }
    return render(req,"tercer_plantilla.html",ctx)
