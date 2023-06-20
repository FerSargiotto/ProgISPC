import Modelo


def ListarProducto():
    con = Modelo.Conectar()
    listado = con.ListarProducto()
    print("\n| ID PRODUCTO   |   NOMBRE PRODUCTO    |   ID RECETA   |")
    for producto in listado:
        print(' ',producto[0],"\t\t",producto[1],"\t\t",producto[2])
        input("Para continuar presione enter")

def InsertarProducto():
    con = Modelo.Conectar()

    nombre = input("\nIngrese el nombre del Producto: ")
    
    nuevoProducto = Modelo.Producto(0,nombre,0)

    con.InsertarProducto(nuevoProducto)
    input("Para continuar presione enter")

def ActualizarProducto():
    con = Modelo.Conectar()
    nombre = input("\nIngrese el nombre del Producto que desea actualizar")
    actualizarProducto= Modelo.Producto(0,nombre,0)
    con.ActualizarProducto(actualizarProducto)
    input("Para continuar presione enter")

def BorrarProducto():
    con = Modelo.Conectar()

    nombre = input("\nIngrese el nombre del Producto que quiere borrar ")
    
    borrarProducto= Modelo.Producto(0,nombre,0)

    con.BorrarProducto(borrarProducto)
    input("Para continuar presione enter")


def ListarProduccion():
    con = Modelo.Conectar()
    listado = con.ListarProduccion()
    print("\n| Fecha   |   ID Producto    |   Cantidad   |")
    for produccion in listado:
        print(' ',str(produccion[0]),"\t\t",produccion[1],"\t\t",str(produccion[2]))
        input("Para continuar presione enter")

def InsertarProduccion():
    con = Modelo.Conectar()

    fecha = input("\nIngrese la fecha de produccion ")
    nombre = input("\nIngrese el nombre del producto ")
    cantidad = input("\nIngrese la Cantidad producida ")
    
    nuevaProduccion= Modelo.Produccion(0000/00/00,nombre,0)

    con.InsertarProduccion(nuevaProduccion)
    input("Para continuar presione enter")


def ActualizarProduccion():
    con = Modelo.Conectar()
    nombre = input("\nIngrese la fecha sobre la cual quiere actualizar la produccion ")
    actualizarProduccion= Modelo.Producto(0000/00/00,nombre,0)
    con.ActualizarProduccion(actualizarProduccion)
    input("Para continuar presione enter")

def BorrarProduccion():
    con = Modelo.Conectar()
    nombre = input("\nIngrese la Fecha sobre la cual quiere borrar la produccion ")
    borrarProduccion= Modelo.Produccion(0000/00/00,nombre,0)
    con.BorrarProduccion(borrarProduccion)
    input("Para continuar presione enter")

def ListarInsumos():
    con = Modelo.Conectar()
    listado = con.ListarInsumos()
    print("\n| ID INSUMOS  |   NOMBRE DE INSUMOS   |   UNIDAD   |")
    for insumos in listado:
        print(' ',insumos[0],"\t\t",insumos[1],"\t\t",insumos[2])
        input("Para continuar presione enter")

def InsertarInsumos():
    con = Modelo.Conectar()
    nombre = input("\nIngrese el nombre del Isumos ")
    unidad = input("\nIngrese la unidad de medida del Insumo ")
    nuevoInsumos= Modelo.Insumos(0,nombre,unidad)
    con.InsertarInsumos(nuevoInsumos)
    input("Para continuar presione enter")

def ActualizarInsumos():  
    con = Modelo.Conectar()
    nombre = input("\nIngrese el nombre del insumo que desea actualizar")
    actualizarInsumos= Modelo.Insumos(nombre)
    con.ActualizarInsumos(actualizarInsumos)
    input("Para continuar presione enter")

def BorrarInsumos(): 
    con = Modelo.Conectar()

    nombre = input("\nIngrese el nombre del Insumo que quiere borrar ")
    
    borrarInsumos= Modelo.Insumos(nombre)

    con.BorrarProduccion(borrarInsumos)
    input("Para continuar presione enter")



def ListarReceta():
    con = Modelo.Conectar()
    listado = con.ListarReceta()
    print("\n| ID RECETA   |   ID PRODUCTO    |   ARINA   |   SAL   |   AZUCAR   |   HUEVO   |   MANTECA   |")
    for producto in listado:
        print(' ',producto[0],"\t\t",producto[1],"\t\t",str(producto[2]),"\t\t",str(producto[3]),"\t\t",str(producto[4]),"\t\t",str(producto[5]),"\t\t",str(producto[6]))
        input("Para continuar presione enter")

def InsertarReceta(): #falta data
    con = Modelo.Conectar()

    nombre = input("\nIngrese Receta ")
    
    nuevaReceta= Modelo.Receta(0,0,0,0,0,0,0)

    con.InsertarReceta(nuevaReceta)
    input("Para continuar presione enter")

def ActualizarReceta():
    con = Modelo.Conectar()
    nombre = input("\nIngrese la ID del producto sobre cual quiere actualizar el ID de receta sobre el cual quiere realizar actualización")
    actualizarReceta = Modelo.Producto(0)
    con.ActualizarProduccion(actualizarReceta)
    input("Para continuar presione enter")

def BorrarReceta(): #falta data
    con = Modelo.Conectar()

    nombre = input("\nIngrese el nuemro de ID de receta que desea borrar")
    
    borrarReceta = Modelo.Receta(0)

    con.BorrarReceta(borrarReceta)
    input("Para continuar presione enter")




