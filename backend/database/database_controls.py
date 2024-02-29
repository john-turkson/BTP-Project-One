import psycopg2
from dotenv import load_dotenv
import os
from flask import jsonify

# Load Environment Variables
load_dotenv()

# Connect to Database
def connect_to_db():
    try:
        # Connect to PostgreSQL Database
        conn = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except Exception as e:
        print("Error connecting to PostgreSQL: ", e)
        return None


# Create Tables Decorator
def db_create_table_decorator(error_message="Error performing Database command!",
                                 success_message="Database command executed successfully!"):
    def decorator(func):
        
        def wrapper(command):
            
            # Get PostgreSQL connection
            postgresConn = connect_to_db()

            if postgresConn:
                
                try:
                    # Open cursor to perform database operations
                    cursor = postgresConn.cursor()
                    
                    # Execute the command
                    cursor.execute(command)
                    
                    # Commit the command
                    postgresConn.commit()

                    # Close cursor and Connection
                    cursor.close()
                    postgresConn.close()

                    print(success_message)
                    
                except Exception as e:
                    
                    print(error_message, e)
                    return None
                
        return wrapper

    return decorator

# Insert Into Tables Decorator
def db_insert_decorator(error_message='', success_message=''):
    
    def decorator(func):
        def wrapper(*args):
            # Connect to PostgreSQL Database
            connection = connect_to_db()

            if connection:
                
                try:
                    # Create Cursor
                    cursor = connection.cursor()

                    # Execute the SQL Command
                    insert_query, insert_values = func(*args)
                    cursor.execute(insert_query, insert_values)

                    # Commit the execution
                    connection.commit()

                    # Close cursor and Connection
                    cursor.close()
                    connection.close()

                    return jsonify({'message': success_message}), 201

                except Exception as e:
                    print("Error executing SQL command:", e)
                    return jsonify({'message': error_message}), 500
            else:
                return jsonify({'message': 'Failed to connect to database'}), 500

        return wrapper

    return decorator
