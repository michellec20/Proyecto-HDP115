from django import template

register = template.Library()

@register.filter
def get_categoria_nombre(value):
    categorias = {
        1: 'Economía',
        2: 'Cambio climático',
    }
    return categorias.get(value, '')