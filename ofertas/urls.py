from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('ofertas/criar/', views.ofertas_criar, name='ofertas_criar'),
    path('trabalheconosco/', views.trabalhe_conosco, name='trabalhe_conosco'),
    path('ofertas/editar<int:id>/', views.ofertas_editar, name='ofertas_editar'),
    path('ofertas/remover<int:id>', views.oferta_remover, name='ofertas_remover'),
    path('ofertas/admin/', views.ofertas_admin, name='ofertas_admin')
]
