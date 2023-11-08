# coding=utf-8
__Author__="Manuel Felipe Sánchez Córdoba"

import random

# Función que determina si un número es par.
def esPar(numero):
    return numero % 2 == 0

# Función que determina si un número es impar.
def esImpar(numero):
    return numero % 2 != 0

# Función que genera una lista de números pares.
def generarPares(valores, inicio):
    pares = []
    numero = inicio
    if esImpar(inicio):
        numero = inicio + 1

    while valores > 0:
        pares.append(numero)
        numero = numero + 2
        valores = valores - 1

    return pares

# Función que genera una lista de números impares.
def generarImpares(valores, inicio):
    impares = []
    numero = inicio
    if esPar(inicio):
        numero = inicio + 1

    while valores > 0:
        impares.append(numero)
        numero = numero + 2
        valores = valores - 1

    return impares

# Programa principal
def main():
    print("Par e impar")
    n = int(input("Introduzca un número: "))
    print("{0} es par --> {1}.".format(n, esPar(n)))
    m = int(input("Introduzca el número de valores: "))
    i = int(input("Introduzca el número inicial: "))
    x = generarPares(m, i)
    y = generarImpares(m, i)
    print("Impares:", y)
    print("Pares:", x)

if __name__ == "__main__":
    main()

