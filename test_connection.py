import pymysql

try:
    connection = pymysql.connect(host='localhost', user='root', password='Chinnu#61012')  # Add your password
    print("Connection successful!")  # This will print if the connection is established
except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
