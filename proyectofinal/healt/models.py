from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Atencion(models.Model):
    day=models.CharField(max_length=10, verbose_name="Horario de atencion")
    created=models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update=models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        verbose_name="Dia laboral"
        verbose_name_plural="Dias laborales"
        ordering=["created"]
    
    def __str__(self):
        return self.day


class Healt(models.Model):
    title=models.CharField(max_length=100,verbose_name="titulo")
    content=models.TextField(verbose_name="contenido")
    image=models.ImageField(verbose_name="imagen", upload_to="healt")
    author=models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    atencion=models.ManyToManyField(Atencion,verbose_name="Atencion")
    created=models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update=models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        verbose_name="Especialidad"
        verbose_name_plural="Especialidades"
        ordering=["-created"]

    def __str__(self):
        return self.title
