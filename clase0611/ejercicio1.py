#condicionales

edad=int(input("Ingrese su edad: "))

if (edad>=18):
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

#condicionales anidadas

estadoAlumno=True
if(estadoAlumno):
    if(edad>=18):
        print("Se puede inscribir en actividades extracurriculares.")
        