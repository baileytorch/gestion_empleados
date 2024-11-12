import datos.conexion_db as conexion

def listado_tipos_empleado():
    consulta = f"""
        SELECT 
            TE.id_tipo_empleado,
            TE.tipo_empleado,
            TE.descripcion_tipo_empleado
        FROM tipos_empleado TE
        WHERE TE.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_tipo_empleado_por_id(id):
    consulta = f"""
        SELECT 
            TE.id_tipo_empleado,
            TE.tipo_empleado,
            TE.descripcion_tipo_empleado
        FROM tipos_empleado TE
        WHERE TE.id_tipo_empleado = {id};
        """
    data = conexion.leer_datos(consulta)
    return data