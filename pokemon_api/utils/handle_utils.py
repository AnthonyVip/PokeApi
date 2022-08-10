import requests
from pokemon_api.models.pokemons import Pokemon
from pokemon_api.utils.poke_utils import PokemonEvolution


class HandleChain:
    def __init__(self):
        self.data = []
        self.evo_count = 0
        self.in_chain = []

    def save_data(self):
        poke_instances = [Pokemon(**_data) for _data in self.data]
        Pokemon.objects.insert(poke_instances, load_bulk=False)

    def var_poke(self, poke: str):
        _test_url = f'https://pokeapi.co/api/v2/pokemon-species/{poke}/'
        response = requests.get(_test_url)
        data = response.json()
        url = data.get('varieties')[0].get('pokemon').get('url')
        response = requests.get(url)
        _new_data = response.json()
        return _new_data

    def get_pokemon_data(self, name: str, chain_id: int):
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        elif response.status_code == 404:
            data = self.var_poke(name)
        else:
            print(name)
            return None

        _tmp_data = {"pokemon_id": int(data.get('id')),
                     "chain_id": chain_id,
                     "evo_id": self.evo_count,
                     "name": name,
                     "height": int(data.get('height')),
                     "weight": int(data.get('weight')),
                     "stats": data.get('stats'),
                     "evolutions": []}
        return _tmp_data

    def make_evolutions(self):
        for _poke in self.data:
            for _evo in self.in_chain:
                if not _evo['is_parallel']:
                    if _poke['evo_id'] != _evo['evo_id']:
                        if _poke['evo_id'] > _evo['evo_id']:
                            _type = PokemonEvolution.get_name(PokemonEvolution.Preevolution)  # noqa: E501
                        else:
                            _type = PokemonEvolution.get_name(PokemonEvolution.Evolution)  # noqa: E501
                        _poke['evolutions'].append({"pokemon_id":
                                                    _evo['pokemon_id'],
                                                    "name": _evo['name'],
                                                    "type": _type})
                else:
                    _main_poke = self.data[0].get('name')
                    if _poke['name'] == _main_poke:
                        _type = PokemonEvolution.get_name(PokemonEvolution.Evolution)  # noqa: E501
                        _poke['evolutions'].append({"pokemon_id":
                                                    _evo['pokemon_id'],
                                                    "name": _evo['name'],
                                                    "type": _type})

    def handle_evolution(self, chain, chain_id, evo_parallel: bool = False):
        _poke = self.get_pokemon_data(chain.get('species').get('name'),
                                      chain_id)
        self.data.append(_poke)
        try:
            self.in_chain.append({"pokemon_id": int(_poke.get('pokemon_id')),
                                  "name": _poke.get('name'),
                                  "evo_id": self.evo_count,
                                  "is_parallel": evo_parallel})
        except AttributeError as e:
            print(chain, chain_id, _poke)
            print(e)
        self.evo_count += 1
        if chain.get('evolves_to'):
            if len(chain.get('evolves_to')) > 1:
                for _chain in chain.get('evolves_to'):
                    self.handle_evolution(_chain, chain_id, True)
            else:
                self.handle_evolution(chain.get('evolves_to')[0], chain_id)
        return True
