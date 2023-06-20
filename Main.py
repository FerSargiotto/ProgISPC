import Controlador

while True:
    print("\n+-------------------------------------------+")
    print("|         Big Bread SA         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - ALTA / BAJA / MODIFICACION DE INSUMOS")
    print("3 - ALTA / BAJA / MODIFICACION DE PRODUCCIÓN DIARIA")
    print("4 - ALTA / BAJA / MODIFICACION DE RECETAS")
    print("5 - LISTADO DE PRODUCTOS")
    print("6 - LISTADO DE INSUMOS ")
    print("7 - LISTADO DE INSUMOS PRODUCCION")
    print("8 - LISTADO DE INSUMOS DE RECETAS")
    print("9 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Controlador.InsertarProducto()
        Controlador.ActualizarProducto()()
        Controlador.BorrarProducto()
    elif opcion == 2:
        Controlador.InsertarInsumos()
        Controlador.ActualizarInsumos()()
        Controlador.BorrarInsumos()
    elif opcion == 3:
        Controlador.InsertarProduccion()
        Controlador.ActualizarProduccion()
        Controlador.BorrarProduccion()
    elif opcion == 4:
        Controlador.InsertarReceta()
        Controlador.ActualizarReceta()
        Controlador.BorrarReceta()

    elif opcion == 5:
        Controlador.ListarProductos()
    elif opcion == 6:
        Controlador.ListarProduccion()
    elif opcion == 7:
        Controlador.ListarInsumos()
    elif opcion == 8:
        Controlador.ListarReceta()
    else:
        print("¡Opción incorrecta!")



