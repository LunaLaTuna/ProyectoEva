
import conexion
import pandas as pd 
import matplotlib.pyplot as plt

cursor = conexion.connection.cursor()


# cursor.execute("SELECT * FROM app_seguimiento_usuario ")



#consulta 1
tipo_orden = cursor.execute("select clasificacion, folio_orden from app_seguimiento_ordenes inner join app_seguimiento_tipoorden ON app_seguimiento_ordenes.id_tipo_ord_id = app_seguimiento_tipoorden.id_tipo_odn ")
tipo_orden = cursor.fetchall()

df_consulta_2= pd.DataFrame(tipo_orden)


df_consulta_2 = df_consulta_2.rename(columns={0: 'Tipo'})
#print(df_consulta_2)

conteo = df_consulta_2.groupby(['Tipo']).size().reset_index(name='Cantidad') #reset_index :  restablecer el índice de un DataFrame después de una operación de agrupamiento (groupby) o conteo y generar otra columna para el resultado


print(conteo)

#consulta 4




#consulta 4


consulta_dos = cursor.execute("select usu_nombre, total_general  from app_seguimiento_detalleorden inner join  app_seguimiento_ordenes o on d.id_ord_id = o.id_ord inner join app_seguimiento_usuario u on o.id_usu_id = u.id_usu where u.id_perfil_id = 2 and o.id_estado_ord_id = 3")



cursor.close()
conexion.connection.close()


#df[0] = pd.to_datetime(df[0]) la fecha la convertimos en datatime pero en el mismo dataframe para poder trabajar con ella 

#df['Mes'] = df[0].dt.to_period('M')  creamos una nueva columna en nuetrsa frame llamada mes, y de la columan 0, tomamos lo valores convierte las fechas en un periodo, por ejemplo con M le decimos que sean en periodos de meses

#df = df.rename(columns={1 : 'Modelo'})

#conteo = df.groupby(['Mes',  'Modelo']).size().reset_index(name='cantidad')#realiza un conteo agrupado combinando las dos colmnas , Mes y Modelos, 
#.size cuenta la cantidad de registros por cada combinacion 

#data frame
#        0                 1
#       fecha_entrda   modelo
#
#


