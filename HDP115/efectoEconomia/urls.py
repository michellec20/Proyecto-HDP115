from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('gestionarNoticia/', views.gestionarNoticia,name='gestionarNoticia'),
    path('agregarNoticia/',views.agregarNoticia, name='agregarNoticia')
]