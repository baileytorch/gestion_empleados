from modelos.empleado import Empleado as empleado
from modelos.tipo_empleado import TipoEmpleado as tipo_empleado
from modelos.rol import Rol as rol
from modelos.pais import Pais as pais
import datos.data_empleados

def listado_empleados():    
    lista_empleados = []
    data = datos.data_empleados.listado_empleados()
    for registro in data:
        nuevo_empleado = empleado()
        nuevo_empleado.id_empleado = registro[0]
        nuevo_empleado.rut_empleado = registro[1]
        nuevo_empleado.nombre_empleado = registro[2]
        nuevo_empleado.fecha_contrato = registro[3]
        nuevo_empleado.salario_empleado = registro[4]
        nuevo_empleado.correo_empleado = registro[5]
        nuevo_empleado.telefono_empleado = registro[6]
        nuevo_empleado.direccion_empleado = registro[7]
        nuevo_empleado.fecha_nacimiento_empleado = registro[8]
        nuevo_tipo_empleado = tipo_empleado()
        nuevo_rol = rol()
        nuevo_pais = pais()
        lista_empleados.append(nuevo_empleado)    
    return lista_empleados