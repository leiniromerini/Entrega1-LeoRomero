# Create views in directory root 

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render 

# Pagina Inicio 
def index(request):
    return render(request, "index.html")          
