from django.shortcuts import render, get_object_or_404, redirect
from .forms import CandidatoForm, ProdutoForm
from .models import Candidato, Produto

def index(request):

    return render(request, 'ofertas/pages/index.html')

def trabalhe_conosco(request):
    if request.method == 'POST':
        file = request.FILES
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CandidatoForm()
            return redirect('index')
    else:
        form = CandidatoForm()
    
    return render(request, 'ofertas/pages/trabalhe_conosco.html', {'form': form})

def ofertas(request):
    ofertas = Produto.objects.all()
    context = {'ofertas': ofertas}
    return render(request, 'ofertas/pages/ofertas.html', context)


def ofertas_criar(request):
    if request.method == 'POST':
        file = request.FILES
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            return redirect('ofertas')
    else:
        form = ProdutoForm()

    return render(request, 'ofertas/pages/form_oferta.html', {'form': form})

def contato(request):

    return render(request, 'ofertas/pages/contato.html')