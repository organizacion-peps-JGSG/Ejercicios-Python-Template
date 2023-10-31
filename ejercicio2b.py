
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)


# Programa principal
def main():
    nombre=input(' ¿Como te llamas? ')
    edad=int(input(f'{nombre}, que edad tienes? '))
    
    if edad <18:
        print(f'{nombre}, eres menor de edad y no puedes conducir')
    else:
        print(f'{nombre}, enorabuena, ya puedes conducir. ')
        
    
    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()
