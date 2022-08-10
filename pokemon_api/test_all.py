import unittest
from pokemon_api.models.pokemons import Pokemon
import requests


class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_pokemon_name = "bulbasaur"
        cls.invalid_pokemon_name = "missingno"
        cls.invalid_pokemon_id = 9999
        cls.valid_pokemon_id = 1
        cls.valid_pokemon_chain_id = 1
        cls.invalid_pokemon_chain_id = 9999

    def test_pokemon_name(self):
        valid_pokemon = Pokemon.objects.filter(name=self.valid_pokemon_name)
        self.assertTrue(len(valid_pokemon))
        self.assertEqual(valid_pokemon[0].name, self.valid_pokemon_name)
        invalid_pokemon = Pokemon.objects.filter(name=self.invalid_pokemon_name)  # noqa: E501
        self.assertFalse(len(invalid_pokemon))

    def test_pokemon_id(self):
        valid_pokemon = Pokemon.objects.filter(pokemon_id=self.valid_pokemon_id)  # noqa: E501
        self.assertTrue(len(valid_pokemon))
        self.assertEqual(valid_pokemon[0].pokemon_id, self.valid_pokemon_id)
        invalid_pokemon = Pokemon.objects.filter(pokemon_id=self.invalid_pokemon_id)  # noqa: E501
        self.assertFalse(len(invalid_pokemon))

    def test_pokemon_chain_id(self):
        valid_pokemon = Pokemon.objects.filter(chain_id=self.valid_pokemon_chain_id)  # noqa: E501
        self.assertTrue(len(valid_pokemon))
        self.assertEqual(valid_pokemon[0].chain_id, self.valid_pokemon_chain_id)  # noqa: E501
        invalid_pokemon = Pokemon.objects.filter(chain_id=self.invalid_pokemon_chain_id)  # noqa: E501
        self.assertFalse(len(invalid_pokemon))


class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_pokemon_name = "bulbasaur"
        cls.invalid_pokemon_name = "missingno"
        cls.valid_pokemon_chain_id = 1
        cls.invalid_pokemon_chain_id = 9999
        cls.pokemon_url = "http://127.0.0.1:8000/api/v1/pokemon/"
        cls.chain_url = "http://127.0.0.1:8000/api/v1/chain/"

    def test_pokemon_endpoint(self):
        valid_pokemon = requests.get(f'{self.pokemon_url}{self.valid_pokemon_name}')  # noqa: E501
        self.assertEqual(valid_pokemon.status_code, 200)
        invalid_pokemon = requests.get(f'{self.pokemon_url}{self.invalid_pokemon_name}')  # noqa: E501
        self.assertEqual(invalid_pokemon.status_code, 404)

    def test_chain_endpoint(self):
        valid_chain = requests.get(f'{self.chain_url}{self.valid_pokemon_chain_id}')  # noqa: E501
        self.assertEqual(valid_chain.status_code, 200)
        invalid_chain = requests.get(f'{self.chain_url}{self.invalid_pokemon_chain_id}')  # noqa: E501
        self.assertEqual(invalid_chain.status_code, 404)
