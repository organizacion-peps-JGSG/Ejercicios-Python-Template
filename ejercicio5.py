# coding=utf-8
__Author__="Marouane Saidi Rahim"

import random

# Función que determina si un numero es par.
def esPar(numero) :
    if numero % 2 == 0:
        return True # --> Implemente código de la función <--
    else:
        return False

def esImpar(numero) :
    if numero % 2 == 0:
        return False # --> Implemente código de la función <--
    else:
        return True

def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    if esImpar(inicio):
        numero=inicio+1
    while valores > 0:
        pares=pares+[numero]
        numero += 2
        valores -= 1
    return pares
    # --> Complete código de la función <--

    

def generarImpares(valores, inicio) :
    impares=[]
    numero=inicio
    if esPar(inicio):
        numero=inicio+1
    while valores > 0:
        impares=impares+[numero]
        numero +=2
        valores -=1
    return impares
    # --> Complete código de la función <--


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
