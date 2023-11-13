# coding=utf-8
__Author__="Marouane Saidi Rahim"


# Función que determina si un numero es primo.

def esPrimo(numero) :
    primo = []
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    
    return True
    
    

    # --> Implemente el código del Bucle <--
    
    # Si tiene solo dos divisores el número es primo     
    if contador == 2 :
        return True
    else :
        return False

# Programa principal
def main():
    print("ES PRIMO")
    n=int(input("Introduzca un numero: "))
    print("{0} es primo --> {1}.".format(n,esPrimo(n)))

if __name__== "__main__" :
   main()
