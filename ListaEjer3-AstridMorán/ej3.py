#Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
#de Sonido debe ser diferente

class Animal():
    def __init__(self,name,raza):
        self.name=name
        self.raza=raza
    def __str__(self):
        pass
#Clases hijas

class Gato(Animal):
    def sonido(self,sound):
        print(f"El gato produce un sonido {sound}")

class Perro(Animal):
    def sonido(self,sound):
        print(f"El perro produce un sonido {sound}")


insert1=Perro("Pancho", "Husky")
insert2=Gato("Whiskas", "Esfinge")
insert1.sonido("Ladrido")
insert2.sonido("Maullido")


