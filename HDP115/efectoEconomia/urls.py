from django.urls import path
from efectoEconomia.views import *
from efectoEconomia import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('gestionarNoticia/',gestionarNoticia.as_view(), name='gestionarNoticia'),
    path('agregarNoticia/',agregarNoticia.as_view(), name='agregarNoticia'),
    path('editarNoticia/<int:idnoticia>/', views.editarNoticia, name='editarNoticia'),
    path('eliminarNoticia/<int:idnoticia>/', views.eliminarNoticia, name='eliminarNoticia'),
]