
contra_sys= '1458as7'
##print(type(contra_sys))
list(contra_sys)

contra_usu=list(input('Ingrese su contraseña:'))

i=0

while i< (len(contra_sys)):
    print(i)
    if (contra_sys[i]== contra_usu[i]):
        i+=1
    else:
        break;


if i== ((len(contra_sys))):
    print('Contraseña es correcta')
else:
    print('Contraseña no es correcta') 
