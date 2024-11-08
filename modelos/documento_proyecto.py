from modelos.proyecto import Proyecto as proyecto

class DocumentoProyecto(proyecto):
    def __init__(self, id_proyecto= 0, id_documento_proyecto = 0, nombre_documento = '', ubicacion_documento = '', habilitado = True):
        super().__init__(id_proyecto)
        self.id_documento_proyecto = id_documento_proyecto
        self.nombre_documento = nombre_documento
        self.ubicacion_documento = ubicacion_documento
        self.habilitado = habilitado