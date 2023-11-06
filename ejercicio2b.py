
# Implementa la función esMayorEdad
def esMayorEdad(edad):
    return edad >= 18

# Programa principal
def main():
    nombre = input('¿Cómo te llamas? ')
    edad = int(input(f'{nombre}, ¿qué edad tienes? '))
    
    if esMayorEdad(edad):
        print(f'{nombre}, ¡enhorabuena! Ya puedes conducir.')
    else:
        print(f'{nombre}, eres menor de edad y no puedes conducir.')

if __name__ == "__main__":
    main()

