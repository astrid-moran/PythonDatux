#Realiza un programa que lea 2 números por teclado y determine los siguientes
#aspectos:
#● Si los dos números son iguales
#● Si los dos números son diferentes
#● Si el primero es mayor que el segundo
#● Si el segundo es mayor o igual que el primero


a=int(input('Ingresar valor 1: '))
b=int(input('Ingresar valor 2: '))

while True:
    print("""Escribe una opcion 
            1)¿Son iguales?
            2)¿Son diferentes? 
            3)¿Primero es mayor que el segundo?
            4)¿Segundo es mayor que el primero
            5)Salir""")
    opcion=input("Escribir la opcion: ")

    if opcion == '1':
        if a==b:
            print("Si")
        else:
            print("No")
    elif opcion == '2':
        if a!=b:
            print('Si')
        else:
            print("No")
    elif opcion == '3':
        if a>b:
            print('Si')
        else:
            print("No")
    elif opcion == '4':
        if a<b:
            print('Si')
        else:
            print("No")
    elif opcion == '5':
        break;
    else:
        print("Ingrese un opcion valida")
