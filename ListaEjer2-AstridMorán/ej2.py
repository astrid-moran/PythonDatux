# 2. Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles

# en cuadrados numero de filas = numero de columnas

filas=int(input("Ingrese el número de filas: "))

for i in range (0,filas):
    for j in range(0,filas):
        print("*", end=" ")
    print(" ")