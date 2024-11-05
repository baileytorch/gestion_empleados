from modelos.empleado_proyecto import EmpleadoProyecto as empleado_proyecto

class RegistroTiempo(empleado_proyecto):
    def __init__(self, id_empleado_proyecto = 0, id_registro_tiempo = 0, fecha_registro = '', tiempo_trabajado = 0, tareas_realizadas = '', observaciones = '', habilitado = True):
        super().__init__(id_empleado_proyecto)
        self.id_registro_tiempo = id_registro_tiempo
        self.fecha_registro = fecha_registro
        self.tiempo_trabajado = tiempo_trabajado
        self.tareas_realizadas = tareas_realizadas
        self.observaciones = observaciones
        self.habilitado = habilitado