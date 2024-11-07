from empleado import Empleado as empleado

class Usuario(empleado):
    def __init__(self, rut_empleado='', correo_empleado='', contrasena_empleado = ''):
        super().__init__(rut_empleado, correo_empleado, contrasena_empleado)