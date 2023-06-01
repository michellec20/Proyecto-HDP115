from django.db import models

tipo_categoria =[
    (1, 'Economía'),
    (2, 'Cambio climático')
]
    
# Create your models here.
class noticia(models.Model):
    idnoticia = models.AutoField(primary_key=True)
    fecha = models.DateField()
    titulo = models.CharField(max_length=200, default="", blank=True)
    contenido = models.TextField(max_length=500, default="", blank=True)
    categoria = models.IntegerField(
        blank=True,
        choices=tipo_categoria
    )