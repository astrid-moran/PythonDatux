#.Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
#impar.

numero=int(input("Ingrese el número a evaluar: "))

residuode2=numero%2

if residuode2 == 0:
    print("Es par")
else:
    print("Es impar")
