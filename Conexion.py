import mysql.connector

class MySQLConect:
    
    def __init__(self, Host, User, Password, Database ):
        self.host = Host
        self.user = User
        self.password = Password
        self.database = Database
        self.connection = None
        self.cursor = None
        
    def conect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password ,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        
        print("Conexion exitosa!")
        
        
    def execute_query(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def insert_data(self, table, values):
        query = f"INSERT INTO {table} VALUES {values}"
        self.cursor.execute(query)
        self.connection.commit()
        
    def update_data(self, table, column, new_value, condition):
        query = (f"UPDATE {table} SET {column} = '{new_value}' WHERE {condition}")
        self.cursor.execute(query)
        self.connection.commit()
        
    def select_data(self, table, id):
        query = f"SELECT * FROM {table} WHERE id = {id}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
            
    def delete_data(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

   
