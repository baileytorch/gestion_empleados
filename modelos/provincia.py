from modelos.region import Region as region

class Provincia(region):    
    def __init__(self, codigo_provincia, nombre_provincia, codigo_region):
        super().__init__(codigo_region)
        self.codigo_provincia = codigo_provincia
        self.nombre_provincia = nombre_provincia
    