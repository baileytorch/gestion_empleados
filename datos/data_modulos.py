import datos.conexion_db as conexion

def listado_empleados():
    consulta = f"""
        SELECT 
            M.id_modulo,
            M.codigo_modulo,
            M.nombre_modulo,
            M.descripcion_modulo
        FROM modulos M
        WHERE M.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_empleado(busqueda):
    consulta = f"""
        SELECT 
            M.id_modulo,
            M.codigo_modulo,
            M.nombre_modulo,
            M.descripcion_modulo
        FROM modulos M
        WHERE M.codigo_modulo = {busqueda}';
        """
    data = conexion.leer_datos(consulta)   
    return data