from django.shortcuts import render, get_object_or_404, redirect
from .forms import CandidatoForm
from .models import Candidato

def index(request):

    return render(request, 'ofertas/pages/index.html')

def trabalhe_conosco(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CandidatoForm()
            return redirect('index')
    else:
        form = CandidatoForm()
    
    return render(request, 'ofertas/pages/trabalhe_conosco.html', {'form': form})

def ofertas(request):

    return render(request, 'ofertas/pages/ofertas.html')

def contato(request):

    return render(request, 'ofertas/pages/contato.html')