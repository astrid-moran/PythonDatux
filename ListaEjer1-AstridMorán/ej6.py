#.Realice un programa que calcule la suma de los números hasta el valor ingresado.

num=int(input('Ingrese valor hasta donde será la suma: '))

i=1
suma=0

while (i<= num):
    suma=suma+i
    i+=1
    #print(suma)

print(f'Valor final de la suma es: {suma}')

