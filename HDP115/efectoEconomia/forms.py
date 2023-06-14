from django import forms
from efectoEconomia.models import noticia

class DateInput(forms.DateInput): 
    input_type = 'date'

#Formulario para Crear Noticia
class NoticiaForm(forms.ModelForm):

    class Meta:
        model = noticia
        fields = ('titulo','autor','fecha','tipo_categoria', 'imagen','contenido')
        widgets = { 
            'fecha': DateInput(), 
            'tipo_categoria': forms.Select(attrs={'class': 'form-control'})
            }
        label = {
            
            'titulo':('Título de la noticia'),
            'autor':('Autor de la noticia'),
            'contenido': ('Contenido de la noticia')
            
        }
        imagen = forms.ImageField(required=False)