from django.shortcuts import render
from .models import Contacto


# Create your views here.
def contactos_index(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/index.html', {'contactos':contactos})
