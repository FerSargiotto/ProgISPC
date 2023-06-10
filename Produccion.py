
class produccion_diaria():
    id =0,
    fecha =0000/00/00,
    producto_id =0,
    antidad =0,

    def __init__(self,fecha,id_producto,cantidad):
        self.Fercha = fecha
        self.ID_producto = id_producto
        self.Cantidad = cantidad
    
    def getfecha(self):
        return self.fecha
    def getid_producto(self):
        return self.id_producto
    def getcantidad(self):
        return self.cantidad
        
    def setfecha(self,fecha):
        self.fecha = fecha
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setcantidad(self,cantidad):
        self.cantidad = cantidad
    