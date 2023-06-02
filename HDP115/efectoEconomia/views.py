from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView
from .mixins import *

# Create your views here.
class index(GroupRequiredMixin, TemplateView):
    group_required = [u'administrador']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        return super().dispatch(request, *args, **kwargs)
    template_name = 'index.html'
