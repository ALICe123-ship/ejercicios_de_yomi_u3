from clases.pokemon import Pokemon

lista_pokemons = []


def buscar_pokemon(nombre):
    for pokemon in lista_pokemons:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


while True:
    print("\n========== MENU ==========")
    print("1. Capturar Pokemon")
    print("2. Entrenar Pokemon")
    print("3. Mostrar informacion de Pokemon")
    print("4. Batalla")
    print("5. Mostrar total de Pokemon")
    print("6. Liberar Pokemon")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del Pokemon: ")
        tipo = input("Tipo: ")
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        salud = int(input("Salud: "))

        nuevo = Pokemon(nombre, tipo, ataque, defensa, salud)
        lista_pokemons.append(nuevo)

    elif opcion == "2":
        nombre = input("Nombre del Pokemon a entrenar: ")
        pokemon = buscar_pokemon(nombre)

        if pokemon:
            cantidad = int(input("¿Cuantas estadisticas desea mejorar? (0-3): "))

            if cantidad == 0:
                pokemon.entrenar()

            elif cantidad == 1:
                e1 = input("Ingrese la estadistica: ")
                pokemon.entrenar(e1)

            elif cantidad == 2:
                e1 = input("Primera estadistica: ")
                e2 = input("Segunda estadistica: ")
                pokemon.entrenar(e1, e2)

            elif cantidad == 3:
                e1 = input("Primera estadistica: ")
                e2 = input("Segunda estadistica: ")
                e3 = input("Tercera estadistica: ")
                pokemon.entrenar(e1, e2, e3)

            else:
                print("Cantidad invalida.")
        else:
            print("Pokemon no encontrado.")

    elif opcion == "3":
        if len(lista_pokemons) == 0:
            print("No hay Pokemon registrados.")
        else:
            for pokemon in lista_pokemons:
                pokemon.mostrar_info()

    elif opcion == "4":
        atacante = input("Nombre del Pokemon atacante: ")
        defensor = input("Nombre del Pokemon defensor: ")

        p1 = buscar_pokemon(atacante)
        p2 = buscar_pokemon(defensor)

        if p1 and p2:
            p1.atacar(p2)
        else:
            print("Uno o ambos Pokemon no existen.")

    elif opcion == "5":
        Pokemon.total_pokemons()

    elif opcion == "6":
        nombre = input("Nombre del Pokemon a liberar: ")

        pokemon = buscar_pokemon(nombre)

        if pokemon:
            lista_pokemons.remove(pokemon)
            del pokemon
        else:
            print("Pokemon no encontrado.")

    elif opcion == "7":
        print("Gracias por usar el simulador.")
        break

    else:
        print("Opcion invalida.")