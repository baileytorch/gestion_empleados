from modelos.empleado import Empleado as empleado
from modelos.rol import Rol as rol
from modelos.modulo import Modulo as modulo
class Usuario(empleado, rol):
    def __init__(self, rut_empleado='', correo_empleado='', contrasena_empleado = '', permisos_rol = '', permisos = [modulo]):
        super().__init__(rut_empleado, correo_empleado, contrasena_empleado)
        super().__init__(permisos_rol)
        self.permisos = permisos