
import conexion

cursor = conexion.connection.cursor()


cursor.execute("SELECT * FROM app_seguimiento_usuario ")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conexion.connection.close()

