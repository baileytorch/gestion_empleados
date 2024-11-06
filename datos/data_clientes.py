
from prettytable import from_db_cursor
from conexion_db import generar_conexion as conexion

def listado_clientes():
    cursor = conexion.cursor()
    cursor.execute(f"""
        SELECT 
            C.id_cliente 'Nº Cliente',
            C.rut_cliente 'Rut Cliente',
            P.gentilicio_pais 'Nacionalidad',
            DATE_FORMAT(C.fecha_nac, '%d/%m/%Y') 'Fecha Nacimiento',
            DATE_FORMAT(C.fecha_def, '%d/%m/%Y') 'Fecha Defunción'
        FROM clientes C
        JOIN paises P ON C.codigo_pais = P.codigo_pais
        """)

    tabla = from_db_cursor(cursor)
    print(tabla)                    
    cursor.close()
    conexion.close()