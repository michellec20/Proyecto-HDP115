from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from .models import noticia
from .forms import NoticiaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import *
from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
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
    def dispatch(self, *args, **kwargs):
        return super(agregarNoticia, self).dispatch(*args, **kwargs)

    template_name = 'agregarNoticia.html'
    model = noticia
    form_class = NoticiaForm

    def get_url_redirect(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return reverse_lazy('home')
    
    def form_valid(self, form, **kwargs):
        context = super().get_context_data(**kwargs)
        noticia = form.save(commit=False)
        
        try:
            form.save()
            messages.success(self.request, 'La noticia fue agregada con exito')
        except Exception:
            noticia.delete()
            messages.success(self.request, 'Ocurrió un error al agregar la noticia')

        return HttpResponseRedirect(self.get_url_redirect())
    
class gestionarNoticia(GroupRequiredMixin, View):
    group_required = [u'administrador']
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = 'gestionarNoticia.html'
    model = noticia
    form_class = NoticiaForm

    def get(self, request):
        noticia_obj = noticia.objects.all()  # Obtén todas las noticias del modelo
        context = {'noticias': noticia_obj}
        return render(request, self.template_name, context)
    
    """def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
        
    def get(self, request):
        noticiasListados = noticia.objects.all()
        messages.success(request, '¡Noticia Listada!')
        return render(request, "gestionarNoticia.html", {"noticias": noticiasListados})
    
    def post(self, request):
        id = request.POST['txtId']
        fecha = request.POST['txtFecha']
        autor = request.POST['txtAutor']
        categoria = request.POST['txtCategoria']
        titulo = request.POST['txtTitulo']

        noticia = noticia.objects.create(
            id=id, fecha=fecha, autor=autor, categoria=categoria, titulo=titulo)
        messages.success(request, '¡Noticia Registrada!')
        return redirect('/')
    
    def edicionNoticia(self, request, id):
        noticia_obj = noticia.objects.get(id=id)
        return render(request, "edicionNoticia.html", {"noticia": noticia_obj})
    
    def editarNoticia(self, request):
        id=request.POST['txtId']
        fecha=request.POST['txtFecha']
        autor=request.POST['txtAutor']
        categoria=request.POST['txtCategoria']
        titulo=request.POST['txtTitulo']

        noticia_obj = noticia.objects.get(id=id)
        noticia_obj.fecha = fecha
        noticia_obj.autor = autor
        noticia_obj.categoria = categoria
        noticia_obj.titulo = titulo
        noticia_obj.save()

        messages.success(request, '¡Noticia Actualizada!')

        return redirect('/')
    
    def eliminarNoticia(request, id):
        noticia_obj = noticia.objects.get(id=id)
        noticia_obj.delete()

        messages.success(request, '¡Noticia Eliminada!')

        return redirect('/')"""
    
    
    
        
