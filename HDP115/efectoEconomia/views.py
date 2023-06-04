from urllib import request
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from .mixins import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class index(GroupRequiredMixin, TemplateView):
    group_required = [u'administrador']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        return super().dispatch(request, *args, **kwargs)
    template_name = 'index.html'

class agregarNoticia(GroupRequiredMixin, CreateView):
    group_required = [u'administrador']
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = 'agregarNoticia.html'
    model = noticia
    form_class = NoticiaForm

    def get_url_redirect(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return reverse_lazy('home')
    
    def form_valid(self, form, **kwargs):
        context=super().get_context_data(**kwargs)
        noticia = form.save(commit=False)
        
        try:
            form.save()
            messages.success(self.request, 'La noticia fue agregada con exito')
        except Exception:
            noticia.delete()
            messages.success(self.request, 'Ocurrió un error al agregar la noticia')
        return HttpResponseRedirect(self.get_url_redirect())
    
    class gestionarNoticia(GroupRequiredMixin, TemplateView):
        group_required = [u'administrador']
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = 'gestionarNoticia.html'
    model = noticia

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
        