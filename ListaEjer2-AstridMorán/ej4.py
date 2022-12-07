#4. Realizar un programa que inserte valores en una lista desde el 1 hasta el 100 saltando en 2 en 2 . Ejemplo : [ 1,3 ,5 ,...]

lista=[]

for i in range(1,101,2):
    lista.append(i)

print(lista)