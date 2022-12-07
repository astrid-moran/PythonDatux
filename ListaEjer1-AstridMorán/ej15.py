a=int(input('Ingresar valor 1: '))
b=int(input('Ingresar valor 2: '))

while True:
    print("""Escribe una opcion 
            1)Saludar
            2)Operación Matemática
            3)Salir""")
    opcion=input("Escribir la opcion: ")

    if opcion == '1':
        print('¡Hola!')
    elif opcion == '2':
        print('La resta es: ',a-b)
    elif opcion == '3':
        break;
    else:
        print("Ingrese un opcion valida")