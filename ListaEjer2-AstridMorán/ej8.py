# 8. Definir una función que imprima los argumentos ingresados desde linea de comandos 
# Nota: Usar import sys.argv => *args

import sys
lista=[]
def ingresado(*args):
    args=sys.argv
    for arg in args:
        print("Argumentos: ",args)
        print("Cantidad de argumentos: ",len(args))
        lista.append(arg)


ingresado(sys.argv)
