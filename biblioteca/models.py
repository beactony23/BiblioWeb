from django.db import models

# Create your models here.

from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=150, verbose_name="Autor")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_lanzamiento = models.DateField(blank=True, null=True, verbose_name="Fecha de publicación")
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True, verbose_name="Portada")
    archivo_pdf = models.FileField(upload_to='libros/', blank=True, null=True, verbose_name="Archivo PDF")

    def __str__(self):
        return self.titulo