from rest_framework import viewsets
from poke.models import Pokemon
from poke.serializers import PokemonSerializer


class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.prefetch_related()
    print(queryset)
    serializer_class = PokemonSerializer