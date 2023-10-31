# coding=utf-8
__Author__="José Gaspar Sánchez García"

import random

# Función que determina si un numero es par.

def esPar(numero):
    if numero % 2 == 0:
        return True # --> Implemente código de la función <--
    return False
def esImpar(numero) :
    if numero % 2 != 0:
        return True
    return False

def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    # --> Complete código de la función <--
    while len(pares) < valores:
        if esPar(numero):
            pares.append(numero)
        numero+=1
    return pares

def generarImpares(valores, inicio):
    impares = []
    numero = inicio
    # --> Complete código de la función <--
    while len(impares) < valores:
        if esImpar(numero):
            impares.append(numero)
        numero += 1
    return impares

# Programa principal
def main():
    print("Par e impar")
    n=int(input("Introduzca un numero: "))
    print("{0} es par --> {1}.".format(n,esPar(n)))
    m=int(input("Introduzca el número de valores: "))
    i=int(input("Introduzca el número inicial: "))
    x=generarPares(m,i)
    y=generarImpares(m,i)
    print("Impares: ",y)
    print("Pares: ",x)

if __name__== "__main__" :
   main()
