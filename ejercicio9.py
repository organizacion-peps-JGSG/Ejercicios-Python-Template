# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    return x + y

def resta(x,y) :
    return x - y

def multiplica(x,y) :
    return x * y

def divide(x,y) :
    if y == 0:
        return "Error: división por cero"
    return x / y

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))

        if opcion == 1 :
            s1=int(input("Introduzca el primer sumando: "))
            s2=int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1,s2,suma(s1,s2)))
        elif opcion == 2 :
            minuendo=int(input("Introduzca el minuendo: "))
            sustraendo=int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo,sustraendo,resta(minuendo,sustraendo)))
       # --> Completa el código fuente del programa <-- 
        elif opcion == 3 :
            multiplicador1=int(input("Introduzca el primer multiplicador: "))
            multiplicador2=int(input("Introduzca el segundo multiplicador: "))
            print("La multiplicación de {0} * {1} = {2}.".format(multiplicador1,multiplicador2,multiplica(multiplicador1,multiplicador2)))
        elif opcion == 4 :
            div1=int(input("Introduzca el primer divisor: "))
            div2=int(input("Introduzca el segundo divisor: "))
            print("La división de {0} * {1} = {2}.".format(div1,div2,divide(div1,div2)))
        elif opcion !=0 :
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()
