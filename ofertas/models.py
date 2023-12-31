from django.db import models


class Categoria_oferta(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Oferta(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_antigo = models.FloatField()
    novo_valor = models.FloatField()
    imagem = models.ImageField(upload_to='media')
    categoria = models.ForeignKey(Categoria_oferta, on_delete=models.SET_NULL, null=True)


class Estado(models.Model):
    nome_estado = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome_estado


class Vaga_emprego(models.Model):
    nome_vaga = models.CharField(max_length=50)
    carga_horaria = models.FloatField()
    salario = models.FloatField()

    def __str__(self):
        return self.nome_vaga


class Candidato(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    curriculo = models.ImageField(upload_to='static/ofertas/img')
    vaga_emprego = models.ForeignKey(Vaga_emprego, on_delete=models.SET_NULL,
                                     null=True, default='')

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True)
    email = models.EmailField()
    telefone = models.IntegerField()
