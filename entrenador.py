import random
import time

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = random.randint(1, 100)
        self._pokedex = []
        self._pokemon_principal = None

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_nivel(self):
        return self.nivel

    def get_pokedex(self):
        return self._pokedex

    def asignar_pokemon_principal(self, pokemon):
        self._pokemon_principal = pokemon
    
    @staticmethod
    def _mostrar_progreso():
        for _ in range(5):
            print("-", end=" ", flush=True)  # Imprimir "-" sin salto de línea
            time.sleep(1)  # Esperar 1 segundos entre cada "-"
        print()  # Para mover a la siguiente línea después de los guiones

    # Método para capturar Pokémon
    def atrapar_pokemon(self, pokemon):
        i = 0
        print(f"Intentando atrapar a {pokemon.nombre}...")
        for _ in range(3):  # Puede hacer 3 ataques para reducir el salvajismo
            i += 1
            print(f"--INTENTO {i}--")
            if self.nivel > pokemon._salvajismo: #Si el salvajismo es bajo, se captura
                print("Salvajismo del oponente menor al Nivel del Entrenador")
                print(f"¡{pokemon.nombre} ha sido atrapado!")
                self._pokedex.append(pokemon)
                return True
            else:
                print(f"--ATAQUE--")
                self._pokemon_principal.ataque_critico(pokemon) #Ataque del Pokemon Principal
                if pokemon.get_vida() <= 0:
                    print(f"{pokemon.nombre} ha sido debilitado. No puede ser atrapado.")
                    return False
                else:
                    pokemon._salvajismo -= pokemon._salvajismo * 0.1 #Diminuye un 10%
                    print(f"{pokemon.nombre} tiene {pokemon.get_vida()} de vida y {pokemon._salvajismo} de salvajismo.")
                
                print(f"--DEFENSA--")
                self._pokemon_principal.defender(pokemon._ataque)
                
                if self._pokemon_principal.get_vida() <= 0:
                    print("El pokemon Principal perdio toda su Vida")
                    print("--SALIO DE LOS INTENTOS--")
                    Entrenador._mostrar_progreso()
                    break
                else:
                    print("Continua")
                    Entrenador._mostrar_progreso()
        print("---------------------------------")
        print("---Se terminaron los Intentos---")
        return False
        
    
    # Mostrar datos del entrenador y su pokédex
    def mostrar_datos(self):
        print(f"Entrenador: {self.nombre}, Nivel: {self.nivel}")
        print("Pokédex:")
        for pokemon in self._pokedex:
            pokemon.mostrar_datos()