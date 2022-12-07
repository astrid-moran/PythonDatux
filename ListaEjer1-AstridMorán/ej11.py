a=int(input('Ingresar valor 1: '))
b=int(input('Ingresar valor 2: '))

while True:
    print("""Escribe una opcion 
            1)Suma
            2)Resta (el primero menos el segundo)
            3)Multiplicacion
            4)Salir""")
    opcion=input("Escribir la opcion: ")

    if opcion == '1':
        print('La suma es: ',a+b)
    elif opcion == '2':
        print('La resta es: ',a-b)
    elif opcion == '3':
        print('La multiplicacion es: ',a*b)
    elif opcion == '4':
        break;
    else:
        print("Ingrese un opcion valida")