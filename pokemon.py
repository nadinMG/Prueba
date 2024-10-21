from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    @abstractmethod
    def __init__(self, nombre, tipo, debilidad):
        self.nombre = nombre  # Público, es accesible desde afuera
        self.tipo = tipo      # Público
        self._vida = 100      # Protegido, no debería modificarse desde afuera
        self._ataque = random.randint(0, 100)   # Protegido
        self._defensa = random.randint(0, 100)  # Protegido
        self._velocidad = random.randint(0, 100) # Protegido
        self._salvajismo = random.randint(0, 100) # Protegido
        self.debilidad = debilidad  # Público

    # Getters y setters para vida (si deseas controlar accesos externos)
    def get_vida(self):
        return self._vida

    def set_vida(self, valor):
        if valor <= 0:
            self._vida = 0
        else:
            self._vida = valor
        print(f"La vida de {self.nombre} ahora es {self._vida}.")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self._vida}")
        print(f"Tipo: {self.tipo}")
        print(f"Ataque: {self._ataque}")
        print(f"Defensa: {self._defensa}")
        print(f"Velocidad: {self._velocidad}")
        print(f"Salvajismo: {self._salvajismo}")

    def ataque_critico(self, oponente):
        if self.tipo == oponente.debilidad:
            if random.random() < 0.7:
                ataque_critico = self._ataque * 1.5
                print(f"Ataque crítico de {ataque_critico} realizado contra {oponente.nombre}!")
                oponente.set_vida(oponente._vida - ataque_critico)  # Usamos set_vida para controlar la vida
                return ataque_critico
            else:
                print(f"{self.nombre} intentó hacer un ataque crítico, pero falló.")
        else:
            print(f"{oponente.nombre} no es débil a este tipo de ataque.")
        # Ataque normal si no hay ataque crítico
        print(f"Ataque normal de {self._ataque}")
        oponente.set_vida(oponente._vida - self._ataque)  # Usamos set_vida para controlar la vida
        return self._ataque

    def defender(self, danio):
        if self._velocidad > 50:
            if random.random() < 0.5:
                print(f"{self.nombre} ha evadido el ataque!")
                return 0
            else:
                print(f"{self.nombre} intentó evadir, pero falló!")
        else:
            print(f"{self.nombre} no tiene suficiente velocidad para evadir.")
            
        danio_recibido = max(danio - self._defensa, 0)
        self.set_vida(self._vida - danio_recibido)
        print(f"{self.nombre} recibió {danio_recibido} de daño.")
        return danio_recibido