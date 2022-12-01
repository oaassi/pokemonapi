from rest_framework import serializers
from poke.models import Pokemon, TypePokemon


# class TypesSerializer(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField()
#
#     def  get_name(self, instance):
#         name = []
#         print(TypePokemon.objects.all())
#         for i in TypePokemon.objects.all():
#             name.append(i.name)
#         return name
#
#
#     class Meta:
#         model = TypePokemon
#         fields = ['name']
#         depth = 1
class PokemonSerializer(serializers.ModelSerializer):
    #
    # types = serializers.SerializerMethodField()
    #
    # def get_Types(self, data):
    #
    #     print(data)
    #
    #     return types

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'cp', 'hp', 'created', 'picture', 'types']
        depth = 1
