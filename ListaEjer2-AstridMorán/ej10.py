#Realizar un programa que realice las siguientes funciones de string al texto.
#-split
#-count
#-find
#-uppercase
#-lowercase

texto="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."

#Para split
split_text=texto.split()

print(split_text)

#Para count

for i in texto:
    print(i, "Se repite ",texto.count(i),"veces")

#Para find
encontrar=texto.find("o") #indica donde se encuentra en indice
print(encontrar)

#Para uppercase()
print(texto.upper())

#Para lowercase()
print(texto.lower())