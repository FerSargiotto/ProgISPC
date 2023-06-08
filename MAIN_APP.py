from Conexion import MySQLConect

def main():
    # Crea una instancia de la clase MySQLConect
    db = MySQLConect(Host="localhost", User="root", Password="153258", Database="db_panaderia")

    # Conecta a la base de datos
    db.conect()

    while True:
        print("Opciones:")
        print("1. Consultar datos")
        print("2. Insertar datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Consultar todos los datos de una tabla")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Consulta de datos
            table = input("Ingrese el nombre de la tabla: ")
            id = input("Ingrese el ID a consultar: ")
            results = db.select_data(table, id)
            print(results)
            
            
        elif opcion == "2":
            # Inserción de datos
            table = input("Ingrese el nombre de la tabla: ")
            values = input("Ingrese los valores a insertar: ")
            db.insert_data(table, values) #Al insertar los valores debe hacerse entre parentesis y aplicando "" a los valores que son string
             
                
        elif opcion == "3":
            # Actualización de datos
            table = input("Ingrese el nombre de la tabla: ")
            column = input("Ingrese el nombre de la columna: ")
            new_value = input("Ingrese el nuevo valor: ")
            condition = input("Ingrese la condición: ")
            db.update_data(table, column, new_value, condition)
            
            
        elif opcion == "4":
            # Eliminación de datos
            table = input("Ingrese el nombre de la tabla: ")
            condition = input("Ingrese la condición: ")
            db.delete_data(table, condition) #Al ingresar la condicion, debe hacerce de la siguiente manera: id = (id del producto)
            
        elif opcion == "5" :
            table = input("Ingrese el nombre de la tabla que quiere consultar: ")  
            query = db.execute_query(f"SELECT * FROM {table}") 
            for row in query:
                print(row)
            
        elif opcion == "6":
            # Salir del programa
            print("Saliendo de la base de datos!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    # Cierra la conexión a la base de datos
    db.close()

if __name__ == "__main__":
    main()
