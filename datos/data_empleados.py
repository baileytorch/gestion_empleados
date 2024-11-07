import datos.conexion_db as conexion

def listado_empleados():
    consulta = f"""
        SELECT 
            E.id_empleado 'Nº',
            E.rut_empleado 'Rut',
            E.nombre_empleado 'Nombre',
            P.gentilicio_pais 'Nacionalidad',
            DATE_FORMAT(E.fecha_contrato, '%d/%m/%Y') 'Fecha Contrato',
            E.salario_empleado 'Sueldo',
            E.correo_empleado 'Correo',
            E.telefono_empleado 'Teléfono',
            E.direccion_empleado 'Dirección',
            TIMESTAMPDIFF(YEAR, E.fecha_nacimiento_empleado, CURDATE()) 'Edad',
            TE.tipo_empleado 'Tipo Empleado',
            R.rol 'Rol',
            IF(E.habilitado = 1, 'Habilitado', 'Deshabilitado') 'Estado'
        FROM empleados E
        JOIN tipos_empleado TE ON E.id_tipo_empleado = TE.id_tipo_empleado
        JOIN roles R ON E.id_rol = R.id_rol
        JOIN paises P ON E.codigo_pais = P.codigo_pais
        WHERE E.habilitado = 1;
        """
    data = conexion.ejecutar_consultas(consulta)
    return data

def buscar_empleado(busqueda):
        consulta = f"""
            SELECT 
                E.id_empleado 'Nº',
                E.rut_empleado 'Rut',
                E.nombre_empleado 'Nombre',
                P.gentilicio_pais 'Nacionalidad',
                DATE_FORMAT(E.fecha_contrato, '%d/%m/%Y') 'Fecha Contrato',
                E.salario_empleado 'Sueldo',
                E.correo_empleado 'Correo',
                E.telefono_empleado 'Teléfono',
                E.direccion_empleado 'Dirección',
                TIMESTAMPDIFF(YEAR, E.fecha_nacimiento_empleado, CURDATE()) 'Edad',
                TE.tipo_empleado 'Tipo Empleado',
                R.rol 'Rol',
                IF(E.habilitado = 1, 'Habilitado', 'Deshabilitado') 'Estado'
            FROM empleados E
            JOIN tipos_empleado TE ON E.id_tipo_empleado = TE.id_tipo_empleado
            JOIN roles R ON E.id_rol = R.id_rol
            JOIN paises P ON E.codigo_pais = P.codigo_pais
            WHERE E.habilitado = 1
                AND E.rut_empleado LIKE '%{busqueda}%'
                OR E.nombre_empleado LIKE '%{busqueda}%'
                OR E.correo_empleado LIKE '%{busqueda}%';
            """
        data = conexion.ejecutar_consultas(consulta)   
        return data