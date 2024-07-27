import mysql.connector
from mysql.connector import errorcode

def create_database():
    config = {
        'user': 'root',       
        'password': 'Nafiad@mysql12',  
        'host': 'localhost'        
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
        
        cursor.close()
        conn.close()
    
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL server: {err}")

if __name__ == "__main__":
    create_database()