estudiantes=['Ann','Juan','Lucia','Pepe','Ramiro']

print('Lista original: ',estudiantes)
print('Tamaño de la lista: ',len(estudiantes))
print('Ultimo elemento: ', estudiantes[-1])

i=0
nuevo=[]
while i<5:
    ulti=estudiantes[-1]
    nuevo.append(ulti)
    estudiantes.pop(-1)
    i+=1

print('Lista invertida: ',nuevo)