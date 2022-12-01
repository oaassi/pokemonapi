from django.db import models


class TypePokemon(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    hp = models.IntegerField(blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    picture = models.CharField(max_length=200)
    types = models.ManyToManyField(TypePokemon)

    def __str__(self):
        return self.name
