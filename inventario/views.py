from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
import datetime
from django.utils.dateparse import parse_date
from . import forms, models


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'inventario/sobre.html')

@login_required
def user(request):

    inve_list =  models.Inventario.objects.all().order_by('-create_at').filter(user=request.user)
    paginator = Paginator(inve_list, 30)
    page = request.GET.get('page')
    inve = paginator.get_page(page)

    cliente_list =  models.Cliente.objects.all().order_by('cliente').filter(user=request.user)
    paginator = Paginator(cliente_list, 30)
    page = request.GET.get('page')
    cliente = paginator.get_page(page)

    produto_list =  models.Produto.objects.all().order_by('-valorTotal').filter(user=request.user)
    paginator = Paginator(produto_list, 30)
    page = request.GET.get('page')
    produto = paginator.get_page(page)

    p = models.Inventario.objects.filter(user=request.user,create_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()

    return render(request, 'inventario/perfil.html', {'inve':inve, 'cliente':cliente, 'produto':produto, 'p':p})




# # # CRUD # # #


@login_required
def exisProduto(request):
    form_Inve = forms.InventarioForm(request.POST or None, request.FILES, user=request.user)

    if form_Inve.is_valid():
        form_Inve = form_Inve.save(commit=False)
        form_Inve.user = request.user
        form_Inve.save()

        messages.info(request, 'Inventario Salvo com Sucesso!')
        return redirect('registers')
    else:
        return render(request, 'inventario/exisProduto.html', {'registrar':form_Inve})

@login_required
def addProduto(request):
    form_Produto = forms.ProdutoForm(request.POST or None, request.FILES)

    if form_Produto.is_valid():
        form_Produto = form_Produto.save(commit=False)
        form_Produto.user = request.user
        form_Produto.save()

        messages.info(request, 'Produto Salvo com Sucesso!')
        return redirect('exisProduto')
    else:
        return render(request, 'inventario/addProduto.html', {'produto':form_Produto})

@login_required
def addCliente(request):
    form_Cliente = forms.ClienteForm(request.POST or None, request.FILES)

    if form_Cliente.is_valid():
        form_Cliente = form_Cliente.save(commit=False)
        form_Cliente.user = request.user
        form_Cliente.save()

        messages.info(request, 'Cliente Salvo com Sucesso!')
        return redirect('exisProduto')
    else:
        return render(request, 'inventario/addCliente.html', {'cliente':form_Cliente})



# READING
@login_required
def registers(request):
    sDate = request.GET.get('start_date')
    eDate = request.GET.get('end_date')

    if sDate and eDate:
        print('OK!')

        # converte em data e adiciona um dia
        eDate = parse_date(eDate) + datetime.timedelta(1)
        
        inventario_list =  models.Inventario.objects.filter(user=request.user, create_at__range=[sDate, eDate])
        paginator = Paginator(inventario_list, 20)
        page = request.GET.get('page')
        inventario = paginator.get_page(page)
        return render(request, 'inventario/registros.html', {'inventario':inventario})
        
    else:
        inventario_list =  models.Inventario.objects.all().order_by('-create_at').filter(user=request.user)
        paginator = Paginator(inventario_list, 20)
        page = request.GET.get('page')
        inventario = paginator.get_page(page)
    return render(request, 'inventario/registros.html', {'inventario': inventario})


@login_required
def clienteView(request, id):
    cView = models.Cliente.objects.get(id=id)
    return render(request, 'inventario/clienteProfile.html', {'cView':cView})

@login_required
def produtoView(request, id):
    pView = models.Produto.objects.get(id=id)
    return render(request, 'inventario/produtoView.html', {'pView':pView})

@login_required
def registroView(request, id):
    iView = models.Inventario.objects.get(id=id)
    return render(request, 'inventario/registroView.html', {'iView':iView})



# UPDATING
@login_required
def clienteEdit(request, id):
    cEdit = models.Cliente.objects.get(id=id)

    if request.method == 'POST':
        form_Cliente = forms.ClienteForm(request.POST, request.FILES, instance=cEdit)
        if form_Cliente.is_valid():
            form_Cliente = form_Cliente.save(commit=False)
            form_Cliente.user = request.user
            form_Cliente.save()

            messages.info(request, 'Cliente Editado com Sucesso!')
            return redirect('user')
    else:
        form_Cliente = forms.ClienteForm(instance=cEdit)

    return render(request, 'inventario/addCliente.html', {'cliente': form_Cliente})


# UPDATING
@login_required
def produtoEdit(request, id):
    pEdit = models.Produto.objects.get(id=id)

    if request.method == 'POST':
        form_Produto = forms.ProdutoForm(request.POST, request.FILES, instance=pEdit)
        if form_Produto.is_valid():
            form_Produto = form_Produto.save(commit=False)
            form_Produto.user = request.user
            form_Produto.save()

            messages.info(request, 'Produto Editado com Sucesso!')
            return redirect('user')
    else:
        form_Produto = forms.ProdutoForm(instance=pEdit)

    return render(request, 'inventario/addProduto.html', {'produto': form_Produto})




    # UPDATING
@login_required
def registroEdit(request, id):
    iEdit = models.Inventario.objects.get(id=id)

    if request.method == 'POST':
        form_Registro = forms.InventarioForm(request.POST, request.FILES, instance=iEdit)
        if form_Registro.is_valid():
            form_Registro = form_Registro.save(commit=False)
            form_Registro.user = request.user
            form_Registro.save()

            messages.info(request, 'Registro Editado com Sucesso!')
            return redirect('user')
    else:
        form_Registro = forms.InventarioForm(instance=iEdit)

    return render(request, 'inventario/exisProduto.html', {'registrar': form_Registro})




@login_required
def clienteDel(request, id):
    remove = models.Cliente.objects.get(id=id)
    remove.delete()
    messages.info(request, 'Cliente e Pertencentes Deletado Sem Problemas!')
    return redirect('user')

@login_required
def produtoDel(request, id):
    remove = models.Produto.objects.get(id=id)
    remove.delete()
    messages.info(request, 'Produto e Pertencentes Deletado Sem Problemas!')
    return redirect('user')

@login_required
def registroDel(request, id):
    remove = models.Inventario.objects.get(id=id)
    remove.delete()
    messages.info(request, 'Registro Deletado Sem Problemas!')
    return redirect('user')

