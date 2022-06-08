# Create views in directory root 

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from productos.models import Productos,Productos_herramientas,Productos_muebles 



# Ofertas index.html 

def ofertas(request):
    search_products_herramientas = Productos_herramientas.objects.filter(clase = "Hogar")
    search_products_muebles = Productos_muebles.objects.filter(tipo = "Hogar")

    if search_products_herramientas.exists() or search_products_muebles.exists():

        context = {"search_products_herramientas":search_products_herramientas,"search_products_muebles":search_products_muebles}
    else:
        context = {'errors_herramientas': f'Disculpe, no se encontro herramientas en oferta','errors_muebles': f'Disculpe, no se encontro muebles en oferta'} 
        
    return render(request, 'index.html', context = context)  

