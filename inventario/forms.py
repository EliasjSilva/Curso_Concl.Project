
#forms.py
from django import forms
from . import models
from django.core.exceptions import ValidationError

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = ['produto', 'notes', 'valorBase', 'valorTotal']

        # widgets = {
        #     'valorBase': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter your Full name',
        #             }
        #     ),
        # }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['cliente', 'endereco', 'contato', 'email', 'observacoes']

    def clean_Cliente(self):
        cliente = self.cleaned_data.get('cliente')
        for instance in models.Cliente.objects.all():
            if instance.cliente == cliente:
                raise forms.ValidationError('Já tem um cliente com o nome ' + cliente)
        return cliente

    
        
class InventarioForm(forms.ModelForm):
    class Meta:
        model = models.Inventario
        fields = ['produto', 'cliente', 'valor_p1', 'valor_p2', 'valorProdutos', 'subTotal', 'combustivel', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filtrar produtos e clientes apenas para o usuário logado
        self.fields['produto'].queryset = models.Produto.objects.filter(user=user)
        self.fields['cliente'].queryset = models.Cliente.objects.filter(user=user)
    # def clean_Value1(self):
    #     value1 = self.cleaned_data.get('valor_p1')
    #     if (value1 == ''):
    #         raise forms.ValidationError('Esse campo não deve ser deixado em branco')
    #     return value1


    # def clean_Value2(self):
    #     value2 = self.cleaned_data.get('valor_p2')
    #     if (value2 == ''):
    #         raise forms.ValidationError('Esse campo não deve ser deixado em branco')
    #     return value2


    # def clean_Value3(self):
    #     value3 = self.cleaned_data.get('combustivel')
    #     if (value3 == ''):
    #         raise forms.ValidationError('Esse campo não deve ser deixado em branco')
    #     return value3