import mysql.connector
from mysql.connector import Error

class CConection:
    @staticmethod
    def ConexionBasedeDatos():
        try:
            connection = mysql.connector.connect(
                user='utxicikqbxg6vmos',  # Cambia esto por tu usuario
                password='x2m3PLJ2i5Q0eXcsnMUF',  # Cambia esto por tu contraseña
                host='bgfsdxuviehae5czy0hh-mysql.services.clever-cloud.com',  # Cambia esto por la dirección IP del servidor MySQL
                database='bgfsdxuviehae5czy0hh',  # Cambia esto por el nombre de tu base de datos
                port='3306',  # Cambia esto si tu MySQL está en otro puerto
                connection_timeout=5,
                ssl_disabled=True  # Habilitar SSL si el servidor lo soporta
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error al conectarse a la base de datos: {e}")
            return None 

