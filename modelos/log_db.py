from modelos.empleado import Empleado as empleado

class LogDB:
    def __init__(self, id_empleado = 0, id_log = 0, fecha_log = '', accion_log = '', tabla_log = '', comentario_log = ''):
        super().__init__(id_empleado)
        self.id_log = id_log
        self.fecha_log = fecha_log
        self.accion_log = accion_log
        self.tabla_log = tabla_log
        self.comentario_log = comentario_log