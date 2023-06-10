
class Receta():
    id =0,
    nombre ="",
    descripcion =0,

    def __init__(self,Id,Nombre, Descripcion):
        self.id = Id
        self.nombre = Nombre
        self.descripcion = Descripcion
        
    def getId(self):
        return self.Id
    def getNombre(self):
        return self.Nombre
    def getaDescrpcion(self):
        return self.Descripcion

    def setId(self,Id):
        self.Id = Id
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setDescripcion(self,Descripcion):
        self.Descripcion = Descripcion
    
    