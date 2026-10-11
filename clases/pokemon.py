class Pokemon:
    contador_pokemons = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.contador_pokemons += 1
        print(f"Pokemon {self.nombre} creado correctamente.")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado.")
        Pokemon.contador_pokemons -= 1

    def entrenar(self, *estadisticas):
        self.nivel += 1

        if len(estadisticas) == 0:
            self.ataque += 5
            self.defensa += 5
            self.salud += 10
        else:
            for estadistica in estadisticas:
                if estadistica.lower() == "ataque":
                    self.ataque += 5
                elif estadistica.lower() == "defensa":
                    self.defensa += 5
                elif estadistica.lower() == "salud":
                    self.salud += 10

        print(f"{self.nombre} ha subido al nivel {self.nivel}.")

    def mostrar_info(self):
        print("\n----- INFORMACION DEL POKEMON -----")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        dano = self.ataque - objetivo.defensa

        if dano < 0:
            dano = 0

        objetivo.salud -= dano

        if objetivo.salud < 0:
            objetivo.salud = 0

        print(f"{self.nombre} ataco a {objetivo.nombre}.")
        print(f"{objetivo.nombre} perdio {dano} puntos de salud.")

    @classmethod
    def total_pokemons(cls):
        print(f"Total de Pokemon creados: {cls.contador_pokemons}")
        
        
        