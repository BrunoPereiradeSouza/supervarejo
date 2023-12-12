import django_filters
from .models import Oferta


class OfertaFilter(django_filters.FilterSet):
    categoria__nome = django_filters.ChoiceFilter()

    class Meta:
        model = Oferta
        fields = ('categoria',)
    