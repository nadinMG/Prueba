from pokemon_hierba import PokemonHierba
from pokemon_fuego import PokemonFuego
from pokemon_agua import PokemonAgua
from entrenador import Entrenador
import random
import time

class App:
    @staticmethod
    def crear_pokemon_aleatorio():
        tipos = [PokemonHierba, PokemonFuego, PokemonAgua]
        nombre = f"Pokemon{random.randint(1, 1000)}"
        return random.choice(tipos)(nombre)
    
    @staticmethod
    def _mostrar_progreso():
        for _ in range(5):
            print("-", end=" ", flush=True)  # Imprimir "-" sin salto de línea
            time.sleep(1)  # Esperar 1 segundos entre cada "-"
        print()  # Para mover a la siguiente línea después de los guiones

    @staticmethod
    def simulacion():
        # Crear entrenador
        nombre_entrenador = input("Ingrese el nombre del entrenador: ")
        entrenador = Entrenador(nombre_entrenador)
        # Crear Pokémon principal del entrenador
        pokemon_principal = App.crear_pokemon_aleatorio()
        print("Pokemon Creado")
        entrenador.asignar_pokemon_principal(pokemon_principal)
        print(f"El Pokémon principal de {entrenador.nombre} es {pokemon_principal.nombre} ({pokemon_principal.tipo}).")
        entrenador._pokedex.append(pokemon_principal)
        
        print("---------------------------------")
        App._mostrar_progreso()
        entrenador.mostrar_datos()
        App._mostrar_progreso()
        print("---------------------------------")
        # Crear 10 Pokémon aleatorios para que el entrenador intente atraparlos
        pokemones_para_atrapar = [App.crear_pokemon_aleatorio() for _ in range(10)]
        
        print("---BATALLA POKEMON---")
        # Intentos de captura
        i = 0
        for pokemon in pokemones_para_atrapar:
            i += 1
            print(f"---BATALLA {i}----")
            print (f"VIDA DEL POKEMON PRINCIPAL {pokemon_principal.nombre} es = {entrenador._pokemon_principal.get_vida()}")
            App._mostrar_progreso()
            if entrenador._pokemon_principal.get_vida() > 0:
                pokemon.mostrar_datos()
                App._mostrar_progreso()
                entrenador.atrapar_pokemon(pokemon)
                App._mostrar_progreso()
            else:
                print("El pokemon Principal perdio toda su Vida")
                break
            
        print("--SALIO DE LAS BATALLAS---")

        App._mostrar_progreso()
        print("--------------------------------")
        # Mostrar los resultados de la simulación
        print("\n--- Resultados Finales ---")
        print(f"Entrenador: {entrenador.nombre}")
        print(f"Nivel: {entrenador.nivel}")
        print(f"Vida del Pokemon Principal: {entrenador._pokemon_principal.get_vida()}")
        print("Pokémon atrapados en la Pokédex:")
        for p in entrenador._pokedex:
            print(f"- {p.nombre} ({p.tipo})")

print("--------------------------------------")
App.simulacion()
print("--------------------------------------")