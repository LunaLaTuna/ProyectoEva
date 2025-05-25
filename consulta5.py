import conexion
import pandas as pd
import matplotlib.pyplot as plt

cursor = conexion.connection.cursor()

cursor.execute("""
    SELECT f.fecha_entrada, d.total_general 
    FROM app_seguimiento_ordenes f 
    INNER JOIN app_seguimiento_detalleorden d ON d.id_ord_id = f.id_ord 
    WHERE f.id_estado_ord_id = 3;
""")

resultados = cursor.fetchall()

df = pd.DataFrame(resultados, columns=['fecha_entrada', 'total_general'])

#se tuvo que convertir el campo total a in valotr numerico exacto para la grafica
df['total_general'] = pd.to_numeric(df['total_general'])

# sacar de la columna de fecha a tipo datetime 
df['fecha_entrada'] = pd.to_datetime(df['fecha_entrada'])
df['mes'] = df['fecha_entrada'].dt.to_period('M')


ingresos_por_mes = df.groupby('mes')['total_general'].sum()


ingresos_por_mes.plot(kind='bar', color='skyblue')
plt.title('Ingresos por Mes')
plt.xlabel('Mes')
plt.ylabel('Ingreso Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

cursor.close()
conexion.connection.close()