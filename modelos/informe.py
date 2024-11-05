from tipo_informe import TipoInforme as tipo_informe
from empleado import Empleado as empleado

class Informe(tipo_informe, empleado):
    def __init__(self, id_tipo_informe = 0, id_empleado = 0, id_informe = 0, fecha_creacion = '', ubicacion_informe = '', habilitado = True):
        super().__init__(id_tipo_informe)
        super().__init__(id_empleado)
        self.id_informe = id_informe
        self.fecha_creacion = fecha_creacion
        self.ubicacion_informe = ubicacion_informe
        self.habilitado = habilitado