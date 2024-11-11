from modelos.provincia import Provincia as provincia

class Comuna(provincia):    
    def __init__(self, codigo_comuna, nombre_comuna, codigo_provincia):
        super().__init__(codigo_provincia)
        self.codigo_comuna = codigo_comuna
        self.nombre_comuna = nombre_comuna