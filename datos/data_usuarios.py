import datos.conexion_db as conexion

def listado_usuarios():
    consulta = f"""
        SELECT
            E.rut_empleado,
            E.correo_empleado,
            R.permisos_rol
        FROM empleados E
        JOIN roles R ON E.id_rol = R.id_rol
        WHERE E.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_usuario(busqueda):
    consulta = f"""
        SELECT
            E.rut_empleado,
            E.correo_empleado,
            E.contrasena_empleado,
            R.permisos_rol
        FROM empleados E
        JOIN roles R ON E.id_rol = R.id_rol
        WHERE E.rut_empleado LIKE '%{busqueda}%'
            OR E.rut_empleado LIKE '%{busqueda}%'
            OR E.correo_empleado LIKE '%{busqueda}%'
            AND E.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)   
    return data