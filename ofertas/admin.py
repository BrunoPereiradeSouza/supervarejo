from django.contrib import admin
from .models import Oferta, Estado, Candidato, Vaga_emprego, Categoria_oferta, Contato, Cidade


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome_estado', 'sigla')


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'endereco', 'estado', 
                    'vaga_emprego')


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'valor_antigo', 'novo_valor', 'imagem', 'categoria')


@admin.register(Vaga_emprego)
class Vaga_empregoAdmin(admin.ModelAdmin):
    list_display = ('nome_vaga', 'carga_horaria', 'salario')


admin.site.register(Categoria_oferta)


admin.site.register(Contato)

admin.site.register(Cidade)