from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('ofertas/', views.OfertaListar.as_view(), name='ofertas'),
    path('ofertas/criar/', views.ofertas_criar, name='ofertas_criar'),
    path('trabalheconosco/', views.trabalhe_conosco, name='trabalhe_conosco'),
    path('trabalheconosco/admin', views.candidato_listar, name='candidato_listar'),
    path('candidato/detalhes/<int:id>', views.candidato_detalhe,name='candidato_detalhe'),
    path('ofertas/editar<int:id>/', views.ofertas_editar, name='ofertas_editar'),
    path('ofertas/remover<int:id>', views.oferta_remover, name='ofertas_remover'),
    path('ofertas/admin/', views.ofertas_admin, name='ofertas_admin'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.usuario_logout, name='logout'),
    path('candidato/remover<int:id>', views.candidato_remover, name='candidato_remover')
]
