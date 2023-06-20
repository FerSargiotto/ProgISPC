import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'sargiotto7',
                db = 'BD_Panaderia'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)
    
    def ListarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Producto"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)         
    
    def InsertarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into productos values(null,%s,null)"

                data = (producto.getnombre(),
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
    
    def ActualizarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "UPDATE Productos set Nombre %s where Nombre = %s "
                data = (producto.getnombre(),
                )
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)   

    def BorrarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "DELETE FROM Productos where Nombre Like %s"
                data = (producto.getid_producto(),
                )
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados      

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)


    def ListarProduccion(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Produccion"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
    
    def InsertarProduccion(self,produccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into Produccion values(0000/00/00,null,%s)"

                data = (produccion.getfecha(),
                        produccion.getcantidad(),
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)


    def ActualizarProduccion(self,produccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "UPDATE Produccion SET Fecha 0000/00/00 WHERE ID_Producto = %s "
                data = (produccion.fecha(),
                        produccion.id_producto(),
                        )

                cursor.execute(senteciaSQL,data)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados


            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)   

    def BorrarProduccion(self,produccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "DELETE FROM Produccion where ID_Producto Like %s"
                data = (produccion.getid_produccion(),
                )
                cursor.execute(senteciaSQL,data)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados      

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarIsumos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Insumos"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)         
    
    def InsertarInsumos(self,insumos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into Insumos values(null,%s,%s)"

                data = (insumos.getnombre(),
                        insumos.getunidad(),
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ActualizarInsumos(self,insumos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "UPDATE Insumos SET Nombre WHERE Nombre = %s "
                data = (insumos.getnombre(),
                        )

                cursor.execute(senteciaSQL,data)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados


            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)   

    def BorrarInsumos(self,insumos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "DELETE FROM Insumos where Nombre Like %s"
                data = (insumos.getnombre(),
                )
                cursor.execute(senteciaSQL,data)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados      

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)


    def ListarReceta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Receta"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)         
    
    def InsertarReceta(self,receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into Receta values(null,null,%s,%s,%s,%s,%s)"

                data = (receta.getarina(),
                        receta.getsal(),
                        receta.getazucar(),
                        receta.gethuevo(),
                        receta.huebo(),
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ActualizarReceta(self,receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "UPDATE Receta set ID_receta %s where ID_Producto = %s "
                data = (receta.getid_receta(),
                        receta.getid_producto()
                )
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)   

    def BorrarReceta(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "DELETE FROM Receta where ID_receta Like %s"
                data = (producto.getid_receta(),
                )
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados      

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

class Producto():
    ID_producto =0,
    Nombre = "",
    Id_receta = 0,

    def __init__(self,id_producto,nombre,id_receta):
        self.ID_producto = id_producto
        self.Nombre =nombre
        self.Id_receta =id_receta
    
    def getid_producto(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.id_producto
    def getnombre(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE_PRODUCTO
        return self.nombre
    def getid_receta(self):
        return self.id_receta
    
    def setid_producto(self,id_producto): #ASIGNO UN VALOR A ESTIBUTO. 
        self.id_producto = id_producto
    def setnombre(self,nombre): #ASIGNO UN VALOR A ESTIBUTO. nombrePRoducto=Harina de arroz.
        self.nombre = nombre
    def setid_receta(self,id_receta):
        self.id_receta = id_receta   


class Produccion():
    Fecha =0000-00-00,
    ID_producto =0,
    Cantidad =0,

    def __init__(self,fecha,id_producto,cantidad):
        self.Fecha = fecha
        self.ID_producto = id_producto
        self.Cantidad = cantidad
    
    def getfecha(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.fecha
    def getid_producto(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE_PRODUCTO
        return self.id_producto
    def getcantidad(self):
        return self.cantidad
    
    def setfecha(self,fecha): #ASIGNO UN VALOR A ESTIBUTO. 
        self.fecha = fecha
    def setid_producto(self,id_producto): #ASIGNO UN VALOR A ESTIBUTO. nombrePRoducto=Harina de arroz.
        self.id_producto = id_producto
    def setcantidad(self,cantidad):
        self.cantidad = cantidad  

class Insumos():
    ID_Insumos = 0,
    Nombre = "",
    Unidad = "",

    def __init__(self,id_insumos,nombre,unidad):
        self.ID_Insumos = id_insumos
        self.Nombre = nombre
        self.Unidad = unidad
    
    def getid_insumos(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.id_insumos
    def getnombre(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE_PRODUCTO
        return self.nombre
    def getid_unidad(self):
        return self.unidad
    
    def setinsumos(self,id_insumos): #ASIGNO UN VALOR A ESTIBUTO. 
        self.id_insumos = id_insumos
    def setnombre(self,nombre): #ASIGNO UN VALOR A ESTIBUTO. nombrePRoducto=Harina de arroz.
        self.nombre = nombre
    def setunidad(self,unidad):
        self.unidad = unidad   


class Receta():
    ID_receta = 0,
    ID_producto = 0,
    Arina = 0,
    Sal = 0,
    Azucar = 0,
    Huevo = 0,
    Manteca = 0,

    def __init__(self,id_receta,id_producto,arina,sal,azucar,huevo,manteca):
        self.ID_receta = id_receta
        self.ID_producto = id_producto
        self.Arina = arina
        self.sal = sal
        self.azucar = azucar
        self.huevo = huevo
        self.manteca = manteca
    
    def getid_receta(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.id_receta
    def getid_producto(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE_PRODUCTO
        return self.id_producto
    def getarina(self):
        return self.arina
    def getsal(self): 
        return self.sal
    def getazucar(self):
        return self.azucar
    def gethuevo(self): 
        return self.huevo
    def getmanteca(self):
        return self.manteca
    

    def receta(self,id_receta,id_insumos,arina,sal,azucar,huevo,manteca):
        self.id_receta = id_receta
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setarina(self,arina):
        self.arina = arina
    def setsal(self,sal):
        self.sal = sal
    def setazucar(self,azucar):
        self.azucar = azucar
    def sethuevo(self,huevo):
        self.huevo = huevo
    def setmanteca(self,manteca):
        self.arina = manteca