from django.urls import re_path as url
from pokemon_api import views as pokemon_views


urlpatterns = [
    url(r'^pokemon/(?P<name>.*)/$', pokemon_views.PokemonView.as_view()),
    url(r'^chain/(?P<chain_id>.*)/$', pokemon_views.EvolutionView.as_view()),
]
