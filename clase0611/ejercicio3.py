#Escribir programa que pida al usuario un numero entero
#y muestre por pantalla si es par o impar

numero=int(input("Ingrese el número: "))

residuode2=numero%2

if residuode2 == 0:
    print("Es par")
else:
    print("Es impar")
