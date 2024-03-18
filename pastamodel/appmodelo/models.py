# appmodelo/models.py
from django.db import models
 
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.TextField()
    endereco = models.TextField()
 
 
def __str__(self):
        return self.nome
 
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return f'Pedido de {self.cliente.nome} com o ID: {self.cliente.id}'
 
   
 
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
 
    def subtotal(self):
        return self.quantidade * self.preco_unitario
 
    def __str__(self):
        return f'Item de {self.pedido.cliente.nome}'