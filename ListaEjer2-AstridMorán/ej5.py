#Definir una función que multiplique 2 números mayores de cero.

def multiplicar(a,b):
    if a>0 and b>0:
        multiplicacion=a*b
        print("La multiplicación es: ", multiplicacion)
    else:
        print("Valores introducidos incorrectos")
    
    #return multiplicacion


numA=int(input("Ingrese el primer número : "))
numB=int(input("Ingrese el segundo número : "))
multiplicar(numA,numB)
