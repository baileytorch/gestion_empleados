
from conexion_db import generar_conexion as conexion

class DataClientes:
    def generar_cursor():
        cursor = conexion.cursor()
        return cursor
        
    def listado_clientes():
        cursor = DataClientes.generar_cursor()
        consulta = f"""
            SELECT 
                C.id_cliente 'Nº Cliente',
                C.rut_cliente 'Rut Cliente',
                P.gentilicio_pais 'Nacionalidad',
                DATE_FORMAT(C.fecha_nac, '%d/%m/%Y') 'Fecha Nacimiento',
                DATE_FORMAT(C.fecha_def, '%d/%m/%Y') 'Fecha Defunción'
            FROM clientes C
            JOIN paises P ON C.codigo_pais = P.codigo_pais
            """
        
        cursor.execute(consulta)
        return cursor