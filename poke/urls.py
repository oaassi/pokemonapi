from django.urls import path, include
from rest_framework import routers
from poke import views


router = routers.DefaultRouter()
router.register('', views.PokemonView)

urlpatterns = [
    path('', include(router.urls)),

]
