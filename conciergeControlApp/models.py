from django.db import models

# Create your models here.
class Produto(models.Model):
    local = models.CharField('Local', max_length=100)
    produto = models.CharField('Produto', max_length=100)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return f'{self.local} {self.produto} {self.estoque}'

class Condomino(models.Model):
    ap = models.IntegerField('Apartamento')
    name = models.CharField('Proprietário', max_length=100)
    fone = models.CharField('Fone', max_length=16)
    inquilino = models.CharField('Inquilino', max_length=100)
    fone_inquilino = models.CharField('Fone Inquilino', max_length=16, null=True)

    def __str__(self):
        return f'{ self.ap } {self.name} {self.fone}'

class Acervo_Portaria(models.Model):
    produto = models.CharField('Produto', max_length=100)
    estoque = models.IntegerField('Estoque')

    def __str__(self):
        return f'{ self.produto } {self.estoque}'