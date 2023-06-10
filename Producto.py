
class Producto():
    id=0,
    nombre = "",
    descripcion ="",
    precio =0,


    def __init__(self,Id,Nombre,Descripcion,Precio):
        self.id = Id
        self.nombre = Nombre
        self.descripcion = Descripcion
        self.precio = Precio

    
    def getid_Id(self):
        return self.Id
    def getNombre(self):
        return self.Nombre
    def getDescripcion(self):
        return self.Descripcion
    def getPrecio(self):
        return self.Precio    
       
    def setid_Id(self,Id):
        self.Id = Id
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setDescripcion(self,Descripcion):
        self.descripcion = Descripcion
    