from modelos.tipo_direccion import TipoDireccion as tipo_direccion

class Direccion(tipo_direccion):
    def __init__(self, id_tipo_direccion = 0, id_direccion = 0, codigo_region = '', codigo_provincia = '', codigo_comuna = '', direccion = '', habilitado = True):
        super().__init__(id_tipo_direccion)
        self.id_direccion = id_direccion
        self.codigo_region = codigo_region
        self.codigo_provincia = codigo_provincia
        self.codigo_comuna = codigo_comuna
        self.direccion = direccion
        self.habilitado = habilitado