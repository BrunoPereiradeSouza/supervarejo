from django.contrib import admin
from .models import Oferta, Estado, Candidato

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'nome_produto', 'valor')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome_estado', 'sigla')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'endereco', 'estado')
