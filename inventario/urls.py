from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('Sobre/', views.about, name = 'about'),
    path('Perfil/', views.user, name = 'user'),
    path('Registros/', views.registers, name = 'registers'),
    path('Registros/Cadastrar-Produto-Existente/', views.exisProduto, name = 'exisProduto'),
    path('Registros/Cadastrar-Novo-Produto/', views.addProduto, name = 'addProduto'),
    path('Registros/Cadastrar-Cliente/', views.addCliente, name = 'addCliente'),
]