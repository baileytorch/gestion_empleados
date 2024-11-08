from modelos.proyecto import Proyecto as proyecto
from modelos.empleado import Empleado as empleado

class EmpleadoProyecto(proyecto, empleado):
    def __init__(self, id_empleado = 0, id_proyecto = 0, id_empleado_proyecto = 0, habilitado = True):
        super().__init__(id_proyecto)
        super().__init__(id_empleado)
        self.id_empleado_proyecto = id_empleado_proyecto
        self.habilitado = habilitado