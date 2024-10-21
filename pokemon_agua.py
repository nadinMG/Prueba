import random
from pokemon import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Agua", "Hierba")

    def ataque_critico(self, oponente):
        if self.tipo == oponente.debilidad:
            ataque_critico = self._ataque * 1.7
            print(f"Ataque crítico de Agua de {ataque_critico} realizado contra {oponente.nombre}!")
            oponente.set_vida(oponente._vida - ataque_critico)  # Usamos set_vida para controlar la vida
            return ataque_critico
        # Ataque normal si no hay ataque crítico
        else:
            print(f"{oponente.nombre} no es débil a este tipo de ataque.")
        print(f"Ataque normal de {self._ataque}")
        oponente.set_vida(oponente._vida - self._ataque) 
        return self._ataque

    def defender(self, danio):
        if random.random() < 0.3:
            print(f"{self.nombre} ha reducido el daño a la mitad!")
            danio = danio / 2
        else: 
            print(f"{self.nombre} no se pudo defender")
        danio_recibido = max(danio - self._defensa, 0)
        self.set_vida(self._vida - danio_recibido)
        return danio_recibido