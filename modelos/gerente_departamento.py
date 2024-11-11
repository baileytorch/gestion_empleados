from modelos.empleado import Empleado as empleado
from modelos.departamento import Departamento as departamento

class GerenteDepartamento(departamento, empleado):
    def __init__(self, id_empleado = 0, id_departamento = 0, id_gerente_departamento = 0, habilitado = True):
        super().__init__(id_empleado)
        super().__init__(id_departamento)
        self.id_gerente_departamento = id_gerente_departamento
        self.habilitado = habilitado