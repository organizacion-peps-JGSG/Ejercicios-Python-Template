# coding=utf-8
__Author__="Manuel Felipe Sánchez Córoba"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# coding=utf-8
__author__ = "Manuel Felipe Sánchez Córoba"

def obtenerCalificacion(nota):
    if nota >= 0 and nota < 3:
        return "Muy deficiente"
    elif nota >= 3 and nota < 5:
        return "Insuficiente"
    elif nota >= 5 and nota < 6:
        return "Suficiente"
    elif nota >= 6 and nota < 7:
        return "Bien"
    elif nota >= 7 and nota < 9:
        return "Notable"
    elif nota >= 9 and nota <= 10:
        return "Sobresaliente"
    else:
        return "Nota fuera de rango"-1


def main():
    n = float(input("Introduzca la nota: "))
    if 0 <= n <= 10:
        calificacion = obtenerCalificacion(n)
        print(f'Calificación: {calificacion}')
    else:
        print("La nota debe estar en el rango de 0 a 10.")

7

if __name__== "__main__" :
   main()
