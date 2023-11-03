from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):

    date_hierarchy = 'create'
    list_filter = ['valorTotal', 'create']
    list_display = ['produto', 'valorBase', 'valorTotal', 'create', 'notes' ]


admin.site.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):

    date_hierarchy = 'data'
    list_filter = ['cliente', 'data']
    list_display = ['produto', 'cliente', 'endereco', 'contato', 'data', 'observacoes']


@admin.register(models.Inventario)
class InventarioAdmin(admin.ModelAdmin):

    date_hierarchy = 'create_at'
    list_filter = ['create_at']
    list_display = ['produto', 'cliente', 'valor_p1', 'valor_p2', 'valorProdutos','subTotal', 'combustivel', 'create_at', 'notes']
