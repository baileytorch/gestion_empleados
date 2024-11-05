from pais import Pais as pais
class Cliente(pais):
    def __init__(self, codigo_pais, id_cliente = 0, rut_cliente = '', razon_social = '', correo_contacto = '', telefono_contacto = '', direccion_cliente = '', habilitado = True):
        super().__init__(codigo_pais)
        self.id_cliente = id_cliente
        self.rut_cliente = rut_cliente
        self.razon_social = razon_social
        self.correo_contacto = correo_contacto
        self.telefono_contacto = telefono_contacto
        self.direccion_cliente = direccion_cliente
        self.habilitado = habilitado