#2. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
#clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
#tener un método para agregar productos y otra para mostrar toda la lista de productos.

def ejercicio2():

    class Producto:
        def __init__(self,name,año):
            self.name=name
            self.año=año
        def __str__(self) -> str:
            return f"El autoparte {self.name} producido en el año {self.año}"

    class Catalogo:
        listaTienda=[]
        def __init__(self,parte):
            self.listaTienda.append(parte)
        def agregar(self, nuevo):
            self.listaTienda.append(nuevo)
        def mostrar(self):
            for item in self.listaTienda:
                print(item)

    p=Producto("Radiador",2010)
    c1=Catalogo(p)
    c1.mostrar
    
ejercicio2()
