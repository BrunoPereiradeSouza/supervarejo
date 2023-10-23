from django.db import models

class Oferta(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor = models.FloatField()
    imagem = models.ImageField()

class Estado(models.Model):
    nome_estado = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome_estado

class Candidato(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    curriculo = models.ImageField(upload_to='static/ofertas/img')

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='static/ofertas/img')
