## bucle for 

lista=[1,2,3,4,5,6,34,1]
list2=["as","asa","as"]

for elemento in lista:
    print("este elemento es iterado",elemento)

for elemento in list2:
    print("este elemento es iterado",elemento)


for posicion,elementoValor in enumerate(lista):
    if posicion==4:
        print("sucede en el primer caso")
    print("enumarate",posicion,elementoValor)

dicx={'k1':1,'k2':2,'k3':3}

for variable1,variable2 in dicx.items():
    print(variable1,variable2)

print("for con strings")
texto="hola mundo"

for index,letra in enumerate(texto):
    print(index,letra)

### funcion rango
## range(puntoinicio,stop,pasos)
#agregar * para pasar a una lista 
a=[*range(0,10,1)]
print(a)

## 
print("for con range")
for i in range(10):
    print(i)

print("entre rangos")

for i in range(20,30):
    print(i)