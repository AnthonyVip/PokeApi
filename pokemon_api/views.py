from django.views import View
from django.http import JsonResponse
from pokemon_api.models.pokemons import Pokemon
from pokemon_api.utils.chain_utils import ChainUitls


class PokemonView(View):
    def get(self, request, name: str):
        _result = Pokemon.objects.filter(name=name)
        if not _result:
            return JsonResponse({"message": "Pokemon not found"}, status=404)

        return JsonResponse(_result[0].to_dict(), status=200)


class EvolutionView(View):
    def get(self, request, chain_id: int):
        _result = Pokemon.objects.filter(chain_id=chain_id)
        all_evo = []
        if not _result:
            _chain_class = ChainUitls()
            if not _chain_class.get_in_chain(chain_id):
                return JsonResponse({"message": "Chain not found"}, status=404)
            _result = Pokemon.objects.filter(chain_id=chain_id)
            if not _result:
                return JsonResponse({"message": "Chain not found"}, status=404)

        for _poke in _result:
            all_evo.append(_poke.to_dict())

        return JsonResponse({"evolutions": all_evo}, status=200)
