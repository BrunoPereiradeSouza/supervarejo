from django.urls import path
from .views import index, contato, ofertas, trabalhe_conosco, ofertas_criar


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('ofertas/', ofertas, name='ofertas'),
    path('ofertas/criar/', ofertas_criar, name='ofertas_criar'),
    path('trabalheconosco/', trabalhe_conosco, name='trabalhe_conosco')
]
