from django import forms
from django.forms import ModelForm
from .models import Candidato, Oferta


class CandidatoForm(ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(),
            'email': forms.EmailInput(),
            'telefone': forms.TextInput(),
            'endereco': forms.TextInput(),
            'estado': forms.Select(),
            'curriculo': forms.FileInput(),
            'vaga_emprego': forms.Select()
        }


class OfertaForm(ModelForm):

    class Meta:
        model = Oferta
        fields = '__all__'
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_antigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'novo_valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem_produto': forms.FileInput(attrs={'class': 'form-control'})
        }
