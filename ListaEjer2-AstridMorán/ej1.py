#1.Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número.

lista= []

#iteracion de lista
for i in range(0,10):
    lista.append(i)

print(lista)

for item in lista:
    if item%2==0:
        print(f"El número {item} es múltiplo de 2")
