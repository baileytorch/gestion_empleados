from modelos.tipo_empleado import TipoEmpleado as tipo_empleado
from modelos.rol import Rol as rol
from modelos.pais import Pais as pais
from modelos.direccion import Direccion as direccion

class Empleado(tipo_empleado, rol, pais, direccion):
    def __init__(self,
            id_tipo_empleado = 0,
            id_rol = 0,
            codigo_pais = 0,
            id_direccion = 0,
            id_empleado = 0,
            rut_empleado = '',
            nombre_empleado = '',
            fecha_contrato = '',
            salario_empleado = 0,
            correo_empleado = '',
            telefono_empleado = '',
            fecha_nacimiento_empleado = '',
            contrasena_empleado = '',
            habilitado = True):
        super().__init__(id_tipo_empleado)
        super().__init__(id_rol)
        super().__init__(codigo_pais)
        super().__init__(id_direccion)
        self.id_empleado = id_empleado
        self.rut_empleado = rut_empleado
        self.nombre_empleado = nombre_empleado
        self.fecha_contrato = fecha_contrato
        self.salario_empleado = salario_empleado
        self.correo_empleado = correo_empleado
        self.telefono_empleado = telefono_empleado
        self.fecha_nacimiento_empleado = fecha_nacimiento_empleado
        self.contrasena_empleado = contrasena_empleado
        self.habilitado = habilitado