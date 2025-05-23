import mysql.connector



try:
    connection = mysql.connector.connect(
        host= '192.168.137.123',
        port= 3306,
        user = 'carlos',
        password  = '011323',
        db='bd_honda'
            )
    if connection.is_connected():
        print("Conexion exitosa")

except Exception as ex:
        print(f"Error en: ", ex)

