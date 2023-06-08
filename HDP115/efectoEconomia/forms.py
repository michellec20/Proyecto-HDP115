from django import forms
from efectoEconomia.models import noticia

class DateInput(forms.DateInput): 
    input_type = 'date'

#Formulario para Crear Noticia
class NoticiaForm(forms.ModelForm):

    class Meta:
        model = noticia
        fields = ('titulo','autor','fecha','tipo_categoria','contenido')
        widgets = { 'fecha': DateInput(), }
        label = {
            
            'titulo':('Título de la noticia'),
            'autor':('Autor de la noticia'),
            'contenido': ('Contenido de la noticia')
            
        }