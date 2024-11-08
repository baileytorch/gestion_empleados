import datos.conexion_db as conexion

def listado_paises():
    consulta = f"""
        SELECT codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais FROM  paises;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_pais(busqueda):
        consulta = f"""
            SELECT codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais FROM  paises
            WHERE codigo_pais = {busqueda};
            """
        data = conexion.leer_datos(consulta)   
        return data