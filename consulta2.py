
import conexion

cursor = conexion.connection.cursor()


cursor.execute("SELECT n.nombre_pieza, e.estado_detalle FROM app_seguimiento_detalleorden d INNER JOIN app_seguimiento_nombrepieza n ON d.codigo_pieza_id = n.id_nombre INNER JOIN app_seguimiento_estadodetalle e ON d.id_estado_detalle_id = e.id_estado_detalle;")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conexion.connection.close()

