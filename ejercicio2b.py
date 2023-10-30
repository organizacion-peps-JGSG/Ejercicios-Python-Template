# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)


# Programa principal
def main():
    nombre=str(input("Dime tu nombre: "))
    edad=int(input("Dime tu edad: "))

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

    esMayorEdad(edad)



def esMayorEdad(e):
    if e>=18:
        print("Ya puedes conducir")
    else:
        print("Todavía no puedes conducir")

if __name__== "__main__" :
   main()
