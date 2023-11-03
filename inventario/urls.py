from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('Sobre/', views.about, name = 'about'),
    path('Perfil/', views.user, name = 'user'),
    path('Registros/', views.registers, name = 'registers'),

    # Registrando os produtos - CREATING
    path('Registros/Cadastrar-Produto-Existente/', views.exisProduto, name = 'exisProduto'),
    path('Registros/Cadastrar-Novo-Produto/', views.addProduto, name = 'addProduto'),
    path('Registros/Cadastrar-Cliente/', views.addCliente, name = 'addCliente'),

    # Listando os Clientes por ID - READING
    path('Perfil/Cliente/<int:id>/', views.clienteView, name='clienteView'),
    path('Perfil/Produto/<int:id>/', views.produtoView, name='produtoView'),
    path('Perfil/Registro/<int:id>/', views.registroView, name='registroView'),
]