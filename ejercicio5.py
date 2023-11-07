# coding=utf-8
__Author__="Manuel Felipe Sánchez Córdoba"

import random

# Función que determina si un numero es par.

def esPar(numero) :
    
   return numero %2 == 0

def esImpar(numero) :
    return numero % 2 !=0

def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    if esImpar(inicio) :
        numero=inicio+1
        
    for a in range(valores):
        pares.append(numero)
        

    return pares

    # --> Complete código de la función <--

    

def generarImpares(valores, inicio):
    impares = []
    numero = inicio

    while len(impares) < valores:
        if not esPar(numero):
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
