from urllib import request
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from .mixins import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import noticia
from django.contrib import messages

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
        
    def home(request):
        noticiasListados = noticia.objects.all()
        messages.success(request, '¡Noticia Listada!')
        return render(request, "gestionarNoticia.html", {"noticias": noticiasListados})
    
    def registrarNoticia(request):
        id=request.POST['txtId']
        fecha=request.POST['txtFecha']
        autor=request.POST['txtAutor']
        categoria=request.POST['txtCategoria']
        titulo=request.POST['txtTitulo']

        noticia = NoticiaForm.objects.create(
        id=id, fecha=fecha, autor=autor, categoria=categoria, titulo=titulo)
        messages.success(request, '¡Noticia Registrada!')
        return redirect('/')
    
    def edicionNoticia(request, id):
        noticia = noticia.objects.get(id=id)
        return render(request, "edicionNoticia.html", {"noticia": noticia})
    
    def editarNoticia(request):
        id=request.POST['txtId']
        fecha=request.POST['txtFecha']
        autor=request.POST['txtAutor']
        categoria=request.POST['txtCategoria']
        titulo=request.POST['txtTitulo']

        noticia = noticia.objects.get(id=id)
        noticia.fecha = fecha
        noticia.autor = autor
        noticia.categoria = categoria
        noticia.titulo = titulo
        noticia.save()

        messages.success(request, '¡Noticia Actualizada!')

        return redirect('/')
    
    def eliminarNoticia(request, id):
        noticia = noticia.objects.get(id=id)
        noticia.delete()

        messages.success(request, '¡Noticia Eliminada!')

        return redirect('/')