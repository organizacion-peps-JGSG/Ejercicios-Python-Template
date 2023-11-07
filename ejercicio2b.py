# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir..

# Implemente función esMayorEdad(e)
def esMayorEdad(edad):
    if edad >= 18:
        return True
    else:
        return False


# Programa principal
def main():
    nombre="Marouane"
    edad=21

    # Utilice la función definida
    if esMayorEdad(edad):
        print("Usted es mayor de edad")
    else:
        print("Todavía eres menor de edad")
    # Estructura alternativa Si (condidición con función) entonces --> sino ...


if __name__== "__main__":
   main()
