from modelos.empleado import Empleado as empleado

class Departamento(empleado):
    def __init__(self, id_empleado = 0, id_departamento = 0, nombre_departamento = '', descripcion_departamento = '', habilitado = True):
        super().__init__(id_empleado)
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento
        self.descripcion_departamento = descripcion_departamento
        self.habilitado = habilitado