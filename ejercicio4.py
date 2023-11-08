# coding=utf-8
__Author__="Manuel Felipe Sánchez Córdoba"




import random

# Función que determina quien gana Piedra, papel o tijera
# 0: Empate.
# 1: Gana Jugador 1.
# 2: Gana Jugador 2.
def quienGana(jugada1, jugada2):
    if jugada1 == jugada2:
        return 0
    elif jugada1 == "piedra" and jugada2 == "tijera":
        return 1
    elif jugada1 == "papel" and jugada2 == "piedra":
        return 1
    elif jugada1 == "tijera" and jugada2 == "papel":
        return 1
    else:
        return 2

# Programa principal
def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1 = input("Introduzca el nombre del Jugador 1: ")
    nombre2 = input("Introduzca el nombre del Jugador 2: ")
    numeroTirada = int(input("Introduzca el número de tiradas: "))

    ganadas1 = 0
    ganadas2 = 0

    for tirada in range(numeroTirada, 0, -1):
        print("Tirada nº", tirada)
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])

        print(nombre1, "ha sacado", j1 + ".")
        print(nombre2, "ha sacado", j2 + ".")

        ganador = quienGana(j1, j2)

        if ganador == 0:
            print("Han empatado.")
        elif ganador == 1:
            print("Gana", nombre1)
            ganadas1 += 1
        elif ganador == 2:
            print("Gana", nombre2)
            ganadas2 += 1
        else:
            print("Error.")

    # Resultado final de todas las tiradas
    if ganadas1 == ganadas2:
        print("HAN EMPATADO")
    else:
        if ganadas1 > ganadas2:
            print("Gana", nombre1)
        else:
            print("Gana", nombre2)

if __name__ == "__main__":
    main()

