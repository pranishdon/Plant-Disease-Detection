import mysql.connector

# Replace with your MySQL server details
host = 'localhost:8888'
user = 'root'
password = ''

def create_database():
    try:
        # Connect to the MySQL server (without specifying the database)
        conn = mysql.connector.connect(host=host, user=user, password=password)

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Create the new database 'user-system'
        cursor.execute("CREATE DATABASE IF NOT EXISTS `MYDB`")

        print("Database 'MYdb' created successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def main():
    create_database()

if __name__ == "__main__":
    main()
