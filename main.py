import mysql.connector
from datos.conexion_db import generar_conexion

conexion = generar_conexion()
cursor = conexion.cursor()
query = "SHOW TABLES;"
cursor.execute(query)
if cursor != None:
    for registro in cursor:
        print(registro)
    cursor.close()
else:
    print("Su búsqueda no arrojó resultados...")
conexion.close()