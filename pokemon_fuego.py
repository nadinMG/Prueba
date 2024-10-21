from pokemon import Pokemon

class PokemonFuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Fuego", "Agua")