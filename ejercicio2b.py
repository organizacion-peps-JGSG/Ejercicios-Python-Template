# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad(edad):
    if (edad>=18):
        print("Usted ya puede conducir")
    else:
        print("Todavía eres menor de edad para conducir")

# Programa principal
def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "))

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...
    esMayorEdad(edad)

if __name__== "__main__" :
   main()
