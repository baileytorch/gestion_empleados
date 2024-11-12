from datos import data_empleados
import negocio.encriptacion
from negocio.negocio_empleados import listado_empleados as listado
import negocio.negocio_usuarios
import negocio.generacion_clave

# data = listado()
# print(data)

negocio.generacion_clave.generacion_clave()
# contrasena = input("Ingrese Contraseña:")
# contrasena_encriptada = ''
# contrasena_encriptada = negocio.encriptacion.encriptar_contrasena(contrasena)

# contrasena = input("Ingrese Contraseña:")
# contrasena_anterior = negocio.encriptacion.desencriptar_contrasena(contrasena_encriptada)
# if contrasena_anterior == contrasena:
#     pass