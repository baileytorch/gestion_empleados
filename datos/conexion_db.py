import mysql.connector
from mysql.connector import errorcode
from auxiliares.constantes import host, user, password, database

def generar_conexion():
    config={
        'user': user,
        'password': password,
        'host': host,
        'database': database
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado para el usuario o la contraseña")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()