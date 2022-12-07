#Realizar un programa que ingrese sus datos personales e imprimirlos

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
DNI=input("Ingrese su DNI: ")

tDNI=list(DNI)
if (len(tDNI))<8:
    print("Número incorrecto de caracteres de DNI")
else:
    print(f'Nombre: {nombre} con edad: {edad} y DNI: {DNI}')
