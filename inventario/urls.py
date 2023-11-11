from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('Sobre/', views.about, name = 'about'),
    path('Perfil/', views.user, name = 'user'),
    path('Registros/', views.registers, name = 'registers'),

    # Registrando - CREATING
    path('Registros/Cadastrar-Produto-Existente/', views.exisProduto, name = 'exisProduto'),
    path('Registros/Cadastrar-Novo-Produto/', views.addProduto, name = 'addProduto'),
    path('Registros/Cadastrar-Cliente/', views.addCliente, name = 'addCliente'),

    # Listando por ID - READING
    path('Perfil/Cliente/<int:id>/', views.clienteView, name='clienteView'),
    path('Perfil/Produto/<int:id>/', views.produtoView, name='produtoView'),
    path('Perfil/Registro/<int:id>/', views.registroView, name='registroView'),

    # Editando por ID
    path('Perfil/Cliente/Editar/<int:id>/', views.clienteEdit, name='clienteEdit'),
    path('Perfil/Produto/Editar/<int:id>/', views.produtoEdit, name='produtoEdit'),
    path('Perfil/Registro/Editar/<int:id>/', views.registroEdit, name='registroEdit'),

    #Deleting por ID
    path('Perfil/Cliente/Deletar/<int:id>/', views.clienteDel, name='clienteDel'),
    path('Perfil/Produto/Deletar/<int:id>/', views.produtoDel, name='produtoDel'),
    path('Perfil/Registro/Deletar/<int:id>/', views.registroDel, name='registroDel'),

]