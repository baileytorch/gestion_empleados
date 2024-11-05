from empleado import Empleado as empleado
from departamento import Departamento as departamento

class EmpleadoDepartamento(departamento, empleado):
    def __init__(self, id_empleado_departamento = 0, id_empleado = 0, id_departamento = 0, habilitado = True):
        super().__init__(id_empleado)
        super().__init__(id_departamento)
        self.id_empleado_departamento = id_empleado_departamento
        self.habilitado = habilitado