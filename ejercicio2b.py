# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)


# Programa principal
def main():
    mayoriaDeEdad = 18
    nombre = input('Escribe tu nombre: ')
    edad = int(getAge(nombre))

    if(esMayorEdad(edad)):
        print(f'Enhorabuena {nombre}, eres mayor de edad')
    else:
        print(f'Lo sentimos {nombre}, eres menor de edad')


def esMayorEdad(age):
    return age >= 18

def promtAge(name):
    return input(f'Escribe tu edad {name}: ')

def getAge(name):
    while True:
        age = promtAge(name)
        if age.isdigit():
            break
        else:
            print("La edad tiene que ser numerica")
    return age

if __name__== "__main__" :
   main()







