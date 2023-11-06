# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    return x

def resta(x,y) :
    return x

def multiplica(x,y) :
    return x

def divide(x,y) :
    if y== 0:
        return "Error: division por cero"
    return x/y

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
        
        try:
        
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
                n1 = int(input("Introduzca el primero numero: "))
                n2 = int(input("Introduzca el segundo numero: "))
                print("La multiplicacion de {0} * {1} = {2}. ".format(n1,n2,multiplica(n1,n2)))
            elif opcion == 4 :
                d1 = int(input("Introduce el primer numero: "))
                d2 = int(input("Introduce el segundo valor: "))
                resultado = divide(d1,d2)
                if resultado == "Error, division por cero":
                    print(resultado)
                else:
                    print("La division {0} / {1} = {2}.".format(d1,d2,resultado))   
            elif opcion == 0: 
                print("Muchas gracias por usar nuestra calculadora !!!!!")
                break;
            else: 
                print("Error, opcion incorrecta")
            
            continuar = input("¿Desea realizar otra operacion ?")
            if continuar.lower() != "si":
                break             
        except ValueError as error:
            print(error)
        except ZeroDivisionError:
            print("Error division por cero")   
        if opcion !=0:
            print("Error, las Opciones ofrecidas van desde 1 hasta 4")      
# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()
