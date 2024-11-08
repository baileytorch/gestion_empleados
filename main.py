from datos import data_empleados
from negocio.negocio_empleados import listado_empleados as listado
import negocio.negocio_usuarios
import negocio.generacion_clave

# data = listado()
# print(data)

# negocio.generacion_clave.generacion_clave()
negocio.negocio_usuarios.test_contrasena(input("Ingrese Contraseña:"))