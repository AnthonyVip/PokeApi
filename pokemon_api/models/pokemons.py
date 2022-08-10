from mongoengine import connect, Document
from mongoengine.fields import StringField, IntField, ListField
from django.conf import settings

connect(settings.MONGO_DB,
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD)


class Pokemon(Document):
    pokemon_id = IntField(required=True)
    name = StringField(required=True)
    height = IntField(required=True)
    weight = IntField(required=True)
    evolutions = ListField(required=True)
    stats = ListField(required=True)
    chain_id = IntField(required=True)
    evo_id = IntField(required=True)

    def to_dict(self):
        return {
            'pokemon_id': self.pokemon_id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'evolutions': self.evolutions,
            'stats': self.stats,
            'chain_id': self.chain_id,
            'evo_id': self.evo_id
        }
