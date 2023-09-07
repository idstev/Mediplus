from django.shortcuts import render
from .models import Client
# Create your views here.
def client(request):
    clientes=Client.objects.all() #queryset-consulta de los registros de servicios
    return render(request, "client/client.html", {'listClientes':clientes})

