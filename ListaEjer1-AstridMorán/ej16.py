#iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad

lista=[['Juan',27],['Janice',15],['Rosa',67],['Tito',13]]

##print(type(lista[1][1]))

i=0
max=len(lista)
print('Mayores de edad son: ')

while i< max:
    if lista[i][1] >=18:
        print(lista[i][0])
    i+=1
    