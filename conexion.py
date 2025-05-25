import mysql.connector



try:
    connection = mysql.connector.connect(
        host= 'localhost',
        port= 3306,
        user = 'root',
        password  = '011323',
        db='bd_honda'
            )
    if connection.is_connected():
        print("Conexion exitosa")

except Exception as ex:
        print(f"Error en: ", ex)

