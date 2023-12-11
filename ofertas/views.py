from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidatoForm, OfertaForm, OfertaFilterForm
from .models import Oferta, Candidato
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator


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
    if request.user.is_authenticated:
        categoria = request.GET.get('categoria')
        ofertas = Oferta.objects.filter(categoria=categoria)
        ofertas_paginator = Paginator(ofertas, 12)
        page_num = request.GET.get('page')
        page = ofertas_paginator.get_page(page_num)
        form = OfertaFilterForm()

        return render(request, 'ofertas/pages/ofertas.html', {'page': page, 'form': form})
    else:
        messages.info(request, 'Você precisa estar logado para ver as ofertas!')
        return redirect('login')


@has_role_decorator('administrador')
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


@has_role_decorator('administrador')
def oferta_remover(request, id):
    oferta = get_object_or_404(Oferta, id=id)
    oferta.delete()
    return redirect('ofertas_admin')


@has_role_decorator('administrador')
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


@has_role_decorator('administrador')
def ofertas_admin(request):
    ofertas = Oferta.objects.all()
    num_ofertas = Oferta.objects.count()
    context = {'ofertas': ofertas, 'num_ofertas': num_ofertas}
    return render(request, 'ofertas/pages/ofertas_admin.html', context)



def cadastrar_usuario(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        e_mail = User.objects.filter(email=email).first()

        if user and e_mail:
            messages.error(request, 'Já existe um usuário com esse nome e email.')
            return redirect('cadastro')
        elif user:
            messages.error(request, 'Já existe um usuário com esse nome.')
            return redirect('cadastro')
        elif e_mail:
            messages.error(request, 'Já existe um usuário com esse email.')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        assign_role(user, 'usuario')

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')

    else:
        return render(request, 'ofertas/pages/cadastro.html')


def login_usuario(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            messages.success(request, 'login realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')
    else:
        return render(request, 'ofertas/pages/login.html')


def usuario_logout(request):
    logout(request)
    return redirect('login')


def candidato_listar(request):
    candidatos = Candidato.objects.all()
    context = {'candidatos': candidatos}
    return render(request, 'ofertas/pages/candidatos_admin.html', context)


def candidato_detalhe(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    context = {'candidato': candidato}
    return render(request, 'ofertas/pages/candidato_detalhe.html', context)
