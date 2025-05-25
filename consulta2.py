import conexion
import pandas as pd
import matplotlib.pyplot as plt
cursor = conexion.connection.cursor()


cursor.execute("SELECT e.estado_detalle, o.fecha_entrada FROM app_seguimiento_detalleorden d INNER JOIN app_seguimiento_estadodetalle e ON d.id_estado_detalle_id = e.id_estado_detalle INNER JOIN app_seguimiento_ordenes o ON d.id_ord_id = o.id_ord WHERE o.id_estado_ord_id = 3; ")

resultados = cursor.fetchall()

df = pd.DataFrame(resultados, columns=['estado_detalle', 'fecha_entrada'])

# Convertir fecha_entrada a datetime y extraer el mes
df['fecha_entrada'] = pd.to_datetime(df['fecha_entrada'])
#df['semana'] = df['fecha_entrada'].dt.isocalendar().week.astype(str)
#df['semana'] = df['fecha_entrada'].dt.to_period('W').astype(str)
#df['mes'] = df['fecha_entrada'].dt.to_period('M').astype(str)
df['semana_inicio'] = df['fecha_entrada'] - pd.to_timedelta(df['fecha_entrada'].dt.weekday, unit='d')
df['semana_inicio'] = df['semana_inicio'].dt.strftime('%d-%m')  # Solo día y mes

# Contar piezas por estado y semana
conteo = df.groupby(['semana_inicio', 'estado_detalle']).size().unstack(fill_value=0)
#conteo = df.groupby(['semana', 'estado_detalle']).size().unstack(fill_value=0)


#  linea
fig, ax = plt.subplots()
conteo.plot(ax=ax, marker='o') 


plt.title('Cantidad de Piezas por Estado y Semana')
plt.xlabel('Semana')
plt.ylabel('Cantidad de Piezas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

