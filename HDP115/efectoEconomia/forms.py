from pyexpat import model
from django import forms
from .models import noticia

class DateInput(forms.DateInput): 
    input_type = 'date'

#Formulario para Crear Noticia
class NoticiaForm(forms.ModelForm):

    class Meta:
        model = noticia
        fields = ('titulo','autor','fecha','categoria','contenido')
        label = {
            
            'titulo':('Título de la noticia'),
            'autor':('Autor de la noticia'),
            'categoria': ('Categoria de la noticia'),
            'contenido': ('Contenido de la noticia')
            
        }
        help_texts ={
           
            'nombre':('Campo obligatorio'),
            'apellido':('Campo obligatorio'),
            
        }