"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "))

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es nayor de edad
    # Sino --> Todavía eres menor de edad

    mayoriaDeEdad = 18
    edad = int(edad)

    if(edad > mayoriaDeEdad):
        print(f'Enhorabuena {nombre}, eres mayor de edad')
    else:
        print(f'Lo sentimos {nombre}, eres menor de edad')






if __name__== "__main__" :
    main()
