from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidatoForm, OfertaForm
from .models import Oferta


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
    ofertas = Oferta.objects.all()
    context = {'ofertas': ofertas}
    return render(request, 'ofertas/pages/ofertas.html', context)


def ofertas_editar(request, id):
    oferta = get_object_or_404(Oferta, id=id)

    if request.method == 'POST':
        form = OfertaForm(request.POST, instance=oferta)

        if form.is_valid():
            form.save()
            return redirect('ofertas_admin')
    else:
        form = OfertaForm(instance=oferta)

    return render(request, 'ofertas/pages/form_oferta.html', {'form': form})


def oferta_remover(request, id):
    oferta = get_object_or_404(Oferta, id=id)
    oferta.delete()
    return redirect('ofertas_admin')


def ofertas_criar(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = OfertaForm()
            return redirect('ofertas_admin')
    else:
        form = OfertaForm()

    return render(request, 'ofertas/pages/form_oferta.html', {'form': form})


def contato(request):

    return render(request, 'ofertas/pages/contato.html')


def ofertas_admin(request):
    ofertas = Oferta.objects.all()
    num_ofertas = Oferta.objects.count()
    context = {'ofertas': ofertas, 'num_ofertas': num_ofertas}
    return render(request, 'ofertas/pages/ofertas_admin.html', context)
