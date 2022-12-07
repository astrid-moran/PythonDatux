#7 Definir una función que retorne el mayor valor al ingresar 2 números.

def BusquedaMayor(a,b):
    if a>b:
        print(f"Mayor valor es: {a}")
    elif a<b:
        print(f"Mayor valor es: {b}")
    elif a==b:
        print(f"Mismos valores, el mayor es: {b}")




numA=int(input("Ingrese el primer número : "))
numB=int(input("Ingrese el segundo número : "))
BusquedaMayor(numA,numB)