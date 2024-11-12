import datos.conexion_db as conexion

def listado_roles():
    consulta = f"""
        SELECT 
            R.id_rol,
            R.rol,
            R.descripcion_rol,
            R.permisos_rol
        FROM roles R
        WHERE R.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_rol_por_id(id):
    consulta = f"""
        SELECT 
            R.id_rol,
            R.rol,
            R.descripcion_rol,
            R.permisos_rol
        FROM roles R
        WHERE R.id_rol = {id};
        """
    data = conexion.leer_datos(consulta)
    return data