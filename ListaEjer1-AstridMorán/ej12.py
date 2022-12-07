val=input('Ingresar letra: ')

list(val)

vocales=['a','e','i','o','u']

if len(val)==1:
    if val in vocales:
        print('Es vocal')
    else:
        print("No es vocal")
else:
    print('No se puede procesar el dato')
