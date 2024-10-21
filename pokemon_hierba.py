from pokemon import Pokemon

class PokemonHierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Hierba", "Fuego")