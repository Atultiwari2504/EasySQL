import pymysql as pm
class EasySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pm.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pm.cursors.DictCursor
            )
            print("Connection successful!")
        except pm.MySQLError as e:
            print(f"Error connecting to MySQL: {e}")
    
    def is_connected(self):
        return self.connection and self.connection.open
    
    def select(self, table, columns='*', where_columns=None, where_values=None, where_operator='AND'):
        if self.is_connected() is False:
            print("Not connected to the database.")
            return

        try:
            if where_columns and where_values:
                if len(where_columns) != len(where_values):
                    print("Error: Number of WHERE columns does not match number of WHERE values.")
                    return
            
            with self.connection.cursor() as cursor:
                if isinstance(columns, list):
                    columns = ", ".join(columns)
                query = f"SELECT {columns} FROM {table}"
                if where_columns and where_values:
                    conditions = [f"{col} = %s" for col in where_columns]
                    query += " WHERE " + f" {where_operator} ".join(conditions)
                    values = where_values or ()
                cursor.execute(query, values)
                results = cursor.fetchall()
                return results
        except pm.MySQLError as e:
            print(f"Error executing SELECT query: {e}")
            return None

    def insert(self, table, columns, data):
        if self.is_connected() is False:
            print("Not connected to the database.")
            return

        try:
            if len(columns) != len(data):
                print("Error: Number of columns does not match number of data values.")
                return
            with self.connection.cursor() as cursor:
                placeholders = ', '.join(['%s'] * len(data))
                column_string = ", ".join(columns)
                query = f"INSERT INTO {table} ({column_string})"
                if placeholders:
                    query += f" VALUES ({placeholders})"
                cursor.execute(query, data)
                self.connection.commit()
                print("Data inserted successfully.")
        except pm.MySQLError as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()
    
    def update(self, table, set_columns, set_values, where_columns=None, where_values=None, where_operator='AND'):
        if self.is_connected() is False:
            print("Not connected to the database.")
            return

        try:
            if where_columns and where_values:
                if len(where_columns) != len(where_values):
                    print("Error: Number of WHERE columns does not match number of WHERE values.")
                    return
            if len(set_columns) != len(set_values):
                print("Error: Number of SET columns does not match number of SET values.")
                return
            if not where_columns:
                print("WHERE clause required")
                return
            with self.connection.cursor() as cursor:
                values = ()
                set_clause = ', '.join([f"{col} = %s" for col in set_columns])
                query = f"UPDATE {table} SET {set_clause}"
                if where_columns and where_values:
                    conditions = [f"{col} = %s" for col in where_columns]
                    query += " WHERE " + f" {where_operator} ".join(conditions)
                    values = set_values + where_values
                cursor.execute(query, values)
                self.connection.commit()
                print("Data updated successfully.")
        except pm.MySQLError as e:
            print(f"Error updating data: {e}")
            self.connection.rollback()

    def delete(self, table, where_columns=None, where_values=None, where_operator='AND'):
        if self.is_connected() is False:
            print("Not connected to the database.")
            return

        try:
            if not where_columns:
                print("Error: No WHERE columns specified.")
                return
            if where_columns and where_values:
                if len(where_columns) != len(where_values):
                    print("Error: Number of WHERE columns does not match number of WHERE values.")
                    return
            with self.connection.cursor() as cursor:
                query = f"DELETE FROM {table}"
                if where_columns and where_values:
                    conditions = [f"{col} = %s" for col in where_columns]
                    query += " WHERE " + f" {where_operator} ".join(conditions)
                    values = where_values or ()
                cursor.execute(query, values)
                self.connection.commit()
                print("Data deleted successfully.")
        except pm.MySQLError as e:
            print(f"Error deleting data: {e}")
            self.connection.rollback()

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
    
    def __del__(self):
        self.close()