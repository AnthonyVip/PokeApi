import os
import django  # noqa
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mo_tech_pokemon.settings")
from pokemon_api.utils.chain_utils import ChainUitls  # noqa


class Populate:
    def __init__(self):
        self.chain_class = ChainUitls()

    def populate(self):
        self.chain_class.get_evolution_chain()


if __name__ == '__main__':
    _populate = Populate()
    _populate.populate()
