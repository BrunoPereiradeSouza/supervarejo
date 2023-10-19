from django import forms
from django.forms import ModelForm
from .models import Candidato

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