from django.db import models
from django.contrib.auth import get_user_model

class Produto(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    valorBase = models.DecimalField(max_digits=10, decimal_places=2, default=1.70)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    create = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-valorTotal']

    def __str__(self):
        return self.produto


class Cliente(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cliente = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    contato = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=150,blank=True,null=True)
    data = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['cliente']

    def __str__(self):
        return self.cliente

class Inventario(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    valor_p1 = models.DecimalField(max_digits=10, decimal_places=2)
    valor_p2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valorProdutos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    combustivel = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-valorProdutos']

    def __str__(self):
        return str(self.valorProdutos)
    
    # # # CÁLCULO # # #
    def save(self, *args, **kwargs):

        self.valorProdutos += self.valor_p1 + self.valor_p2
        self.subTotal += (self.valor_p1 + self.valor_p2) * self.produto.valorBase
        self.produto.valorTotal += self.subTotal
        self.produto.save()

        return super(Inventario, self).save(*args, **kwargs)