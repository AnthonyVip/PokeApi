import enum


class PokemonEvolution(enum.Enum):
    """
    Enum for Pokemon Evolution
    """
    Preevolution = 1
    Evolution = 2

    @classmethod
    def get_name(cls, value):
        return cls(value).name

    @classmethod
    def get_value(cls, name):
        return cls[name].value
