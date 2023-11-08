# coding=utf-8
__Author__="Manuel Felipe Sánchez Córdoba"


# Función que determina si un numero es primo.

def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
        return vector
    elif n == 2:
        vector.append(1)
        vector.append(1)
    else:
        vector.append(1)
        vector.append(1)
        for i in range(2, n):
            next_term = vector[i - 1] + vector[i - 2]
            vector.append(next_term)

    return vector

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un numero: "))
    if numero < 1:
        print("Por favor, introduzca un número mayor o igual a 1.")
    else:
        fib_sequence = fibonacci(numero)
        print("{0} elementos --> FIBONACCI: {1}.".format(numero, fib_sequence))

if __name__ == "__main__":
    main()