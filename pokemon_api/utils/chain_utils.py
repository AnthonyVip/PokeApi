from django.conf import settings
import requests
from pokemon_api.utils.handle_utils import HandleChain
from time import sleep


class ChainUitls:
    def __init__(self):
        self.api_chain_base_url = settings.API_CHAIN_BASE_URL
        self.api_pokemon_base_url = settings.API_POKEMON_BASE_URL
        self.max_evo_ids = settings.MAX_CHAIN_IDS

    def get_in_chain(self, chain_id):
        self.handle_chain = HandleChain()
        url = f'{self.api_chain_base_url}{chain_id}'
        response = requests.get(url)
        if response.status_code != 200:
            return False
        data = response.json()
        self.handle_chain.handle_evolution(data.get('chain'), chain_id)
        self.handle_chain.make_evolutions()
        self.handle_chain.save_data()
        return True

    def get_evolution_chain(self):
        for i in range(1, self.max_evo_ids + 1):
            self.handle_chain = HandleChain()
            url = self.api_chain_base_url + str(i)
            response = requests.get(url)
            if response.status_code != 200:
                print('Error: {}'.format(response.status_code))
                print(i)
                continue
            data = response.json()
            self.handle_chain.handle_evolution(data.get('chain'), i)
            self.handle_chain.make_evolutions()
            self.handle_chain.save_data()
            sleep(0.2)
