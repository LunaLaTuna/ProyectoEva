
import conexion

cursor = conexion.connection.cursor()


cursor.execute(" SELECT f.fecha_entrada, d.total_general FROM app_seguimiento_ordenes f INNER JOIN app_seguimiento_detalleorden d ON d.id_ord_id = f.id_ord; ")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conexion.connection.close()

