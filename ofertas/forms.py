from django import forms
from django.forms import ModelForm
from .models import Candidato, Produto

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
            'curriculo': forms.FileInput()
        }

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem_produto': forms.FileInput(attrs={'class': 'form-control'})
        }