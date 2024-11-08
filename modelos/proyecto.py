from modelos.cliente import Cliente as cliente
from modelos.departamento import Departamento as departamento

class Proyecto(cliente, departamento):
    def __init__(self, id_cliente = 0, id_departamento = 0, id_proyecto = 0, nombre_proyecto = '', descripcion_proyecto = '', fecha_inicio_proyecto = '', fecha_fin_proyecto = '', habilitado = True):
        super().__init__(id_cliente)
        super().__init__(id_departamento)
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.descripcion_proyecto = descripcion_proyecto
        self.fecha_inicio_proyecto = fecha_inicio_proyecto
        self.fecha_fin_proyecto = fecha_fin_proyecto
        self.habilitado = habilitado