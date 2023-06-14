from django.db import models

tipo_categoria =[
    (1, 'Economía'),
    (2, 'Cambio climático')
]
    
# Create your models here.
class noticia(models.Model):
    idnoticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, default="", blank=True)
    autor = models.CharField(max_length=100, default="", blank=True)
    fecha = models.DateField()
    tipo_categoria = models.IntegerField(
        blank=True,
        choices=tipo_categoria
    )
    contenido = models.TextField(max_length=500, default="", blank=True)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.titulo)