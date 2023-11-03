from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidatoForm, ProdutoForm
from .models import Produto


def index(request):

    return render(request, 'ofertas/pages/index.html')


def trabalhe_conosco(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CandidatoForm()
            return redirect('index')
    else:
        form = CandidatoForm()
    return render(request, 'ofertas/pages/trabalhe_conosco.html', 
                  {'form': form})


def ofertas(request):
    ofertas = Produto.objects.all()
    context = {'ofertas': ofertas}
    return render(request, 'ofertas/pages/ofertas.html', context)


def ofertas_editar(request, id):
    oferta = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=oferta)

        if form.is_valid():
            form.save()
            return redirect('ofertas')
    else:
        form = ProdutoForm(instance=oferta)

    return render(request, 'ofertas/pages/for_oferta.html', {'form': form})


def ofertas_criar(request):
    if request.method == 'POST':
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
