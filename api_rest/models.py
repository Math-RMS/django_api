from django.db import models

# Create your models here.

class Produto(models.Model):
    
    produto_nome = models.CharField(max_length=100, default='')
    produto_valor = models.FloatField(default='')
    produto_quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'Nome: {self.produto_nome} | Valor: {self.produto_valor}'