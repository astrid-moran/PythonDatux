#11.Definir los atributos y métodos de una de las siguientes clases.
#- Persona
#- Gato
#- Producto

class Persona:
    def __init__(self,name,edad):
        self.name=name
        self.edad=edad
    def nameSpace(self):
        print(self.name)
    def callEdad(self,dni):
        self.dni=dni


c1=Persona("Jose","24")
c2=Persona("Maria","12")

#print(c1)

class Gato:
    def __init__(self,name,edad,color):
        self.name=name
        self.edad=edad
        self.color=color
    def colorGato(self):
        print(self.color)
   
g1=Gato("Pepillo","2","Naranja")

class Producto:
    def __init__(self,name,marca,categoria):
        self.name=name
        self.marca=marca
        self.categoria=categoria
    def nameMarca(self):
        print(self.marca)

p1=Producto("Jabon","Avon","Aseo")
print(p1.categoria)