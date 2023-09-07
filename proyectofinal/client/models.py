
from django.db import models


# Create your models here.

class Client (models.Model):
    title=models.CharField(max_length=100, verbose_name="titulo")
    image=models.ImageField(verbose_name="imagen", upload_to="client")
    content=models.TextField(verbose_name="contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update=models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
        ordering=["-created"]
    
    def __str__(self):
        return self.title

