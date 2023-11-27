from django import forms
from django.forms import ModelForm
from .models import Candidato, Oferta, Usuario


class CandidatoForm(ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'vaga_emprego': forms.Select(attrs={'class': 'form-control'})
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


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'})
        }
