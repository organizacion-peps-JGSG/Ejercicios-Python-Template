# coding=utf-8
__Author__="José Gaspar Sánchez García"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# Implemente función obtenerCalificacion
def obtenerCalificaion(nota) :
    calificacion="Incorrecta"
   # Implemente aquí ... Si (condición) entonces ... sino ... si (condición) entonces ... sino ...

    if nota in range(0,3):
        return "Muy deficiente"

    elif nota in range(3,5):
        return "Insuficiente"

    elif nota in range(5, 6):
        return "Suficiente"

    elif nota in range(6, 7):
        return "Bien"

    elif nota in range(7, 9):
        return "Notable"

    elif nota in range(9, 11):
        return "Sobresaliente"

    return calificacion

# Programa principal
def main():
    n=int(input("Introduzca la nota: "));
    print('Calificación: '+obtenerCalificaion(n));
if __name__== "__main__" :
   main()
