from Conexion import Conectar


class insumos():
    id =0,
    nombre = "",
    descripcion ="",
    cantidad = 0,

    def __init__(self,Id,Nombre,Descripcion,Cantidad):
        self.id = Id
        self.nombre = Nombre
        self.descripcion = Descripcion
        self.cantidad = Cantidad
    
    def getId(self):
        return self.Id
    def getNombre(self):
        return self.Nombre
    def getDescripcion(self):
        return self.Descripcion
    def getCantidad(self):
        return self.Cantidad
        
    def setId(self,Id):
        self.Id = Id
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setDescripcion(self,Descripcion):
        self.Descripcion = Descripcion   