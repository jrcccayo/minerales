import flet as ft
from flet import *
import mysql.connector
from Conexionuno import CConection


def mostrar_mensaje(page, mensaje, tipo="error"):
        
        page =page
        """
        Muestra un mensaje en un SnackBar.
        
        Parámetros:
            mensaje (str): El mensaje a mostrar.
            tipo (str): Tipo de mensaje ("éxito", "error" o "advertencia").
        """
        # Definir el color de fondo según el tipo de mensaje
        if tipo == "éxito":
            color_fondo = ft.colors.with_opacity(0.7, ft.colors.GREEN)  # 70% de opacidad
        elif tipo == "advertencia":
            color_fondo = ft.colors.with_opacity(0.7, ft.colors.TEAL)   # 70% de opacidad
        else:  # Por defecto, es un error
            color_fondo = ft.colors.with_opacity(0.7, ft.colors.RED)    # 70% de opacidad
        
        # Crear el contenido del SnackBar con bordes redondeados y transparencia
        snack_content = ft.Container(
            content=ft.Text(mensaje, size=18, color=ft.colors.WHITE),  # Texto del mensaje en blanco
            bgcolor=color_fondo,                              # Color de fondo con transparencia
            border_radius=10,                                 # Bordes redondeados de 10
            padding=10,                                       # Espaciado interno
        )
        
        # Crear el SnackBar
        snack_bar = ft.SnackBar(
            content=snack_content,  # Usar el contenedor con bordes redondeados y transparencia
            open=True,              # Abrir automáticamente
            duration=5000,          # Duración de 5 segundos
            bgcolor=ft.colors.TRANSPARENT,  # Fondo transparente para el SnackBar
        )
        
        # Agregar el SnackBar a la página y actualizar la UI
        page.overlay.append(snack_bar)
        page.update()



class CClientes:
    
    @staticmethod
    def mostrarClientes():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Clientes;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error al mostrar clientes: {error}'

    @staticmethod
    def IngresarClientes(page, Denominacion, Departamento, Municipio, Codigo_Municipio, Nim, Precio, Cns, Comibol, Fencomin, Fedecomin, Regalias, Cooperativa, Comunidad, Deporte, Afp):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """INSERT INTO Clientes VALUES (
                        NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )"""
                    valores = (Denominacion, Departamento, Municipio, Codigo_Municipio, Nim, Precio, Cns, Comibol, Fencomin, Fedecomin, Regalias, Cooperativa, Comunidad, Deporte, Afp)
                    cursor.execute(sql, valores)
                    cone.commit()  # Commit necesario para operaciones de inserción
                    
                    # Mostrar mensaje de éxito
                    mostrar_mensaje(page, f"La Cooperativa '{Denominacion}' se ha creado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"La Cooperativa '{Denominacion}' ya existe: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"La Cooperativa '{Denominacion}' ya existe: {error}", tipo="error")

    @staticmethod
    def ModificarClientes(page, IdClientes, Denominacion, Departamento, Municipio, Codigo_Municipio, Nim, Precio, Cns, Comibol, Fencomin, Fedecomin, Regalias, Cooperativa, Comunidad, Deporte, Afp):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Clientes SET
                        Denominacion = %s,
                        Departamento = %s,
                        Municipio = %s,
                        Codigo_Municipio = %s,
                        Nim = %s,
                        Precio = %s,
                        Cns = %s,
                        Comibol = %s,
                        Fencomin = %s,
                        Fedecomin = %s,
                        Regalias = %s,
                        Cooperativa = %s,
                        Comunidad = %s,
                        Deporte = %s,
                        Afp = %s
                    WHERE IdClientes = %s;"""
                    
                    valores = (Denominacion, Departamento, Municipio, Codigo_Municipio, Nim, Precio, Cns, Comibol, Fencomin, Fedecomin, Regalias, Cooperativa, Comunidad, Deporte, Afp, IdClientes)
                    cursor.execute(sql, valores)
                    cone.commit()  # Commit necesario para operaciones de actualización
                    
                    # Mostrar mensaje de éxito
                    mostrar_mensaje(page, f"La Cooperativa '{Denominacion}' se ha actualizado correctamente", tipo="éxito")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error al actualizar la cooperativa: {error}", tipo="error")
    
    @staticmethod
    def EliminarClientes(page, idClientes, Denominacion):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Clientes WHERE IdClientes = %s;"
                    valores = (idClientes,)
                    cursor.execute(sql, valores)
                    cone.commit()  # Commit necesario para operaciones de eliminación
                    
                    # Mostrar mensaje de éxito
                    mostrar_mensaje(page, f"La Cooperativa '{Denominacion}' se ha eliminado exitosamente", tipo="éxito")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"error. No se eliminaron los registros: {error}", tipo="error")
    

class CComprobantes:
    @staticmethod
    def mostrarComprobantes():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Comprobantes ORDER BY IdComprobantes DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarComprobantes(page, IdComprobantes,TipoGasto, FechaComp, NumLote, NombresApellidos, Glosa, Ingreso, Egreso, Saldocaja):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Comprobantes VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
                    valores = (TipoGasto, FechaComp, NumLote, NombresApellidos, Glosa, Ingreso, Egreso, Saldocaja)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Comprobante '{IdComprobantes}' se ha Recepcionado exitosamente", tipo="éxito")
                    return cursor.lastrowid  # Return the ID of the inserted record
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El Comprobante '{IdComprobantes}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El Comprobante '{IdComprobantes}' {error}", tipo="error")            
            return None

    @staticmethod
    def ModificarComprobante(page, TipoGasto, FechaComp, NumLote, NombresApellidos, Glosa, Ingreso, Egreso, Saldocaja, IdComprobantes):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "UPDATE Comprobantes SET TipoGasto = %s, FechaComp = %s, NumLote = %s, NombresApellidos = %s, Glosa = %s, Ingreso = %s, Egreso = %s, Saldocaja = %s WHERE IdComprobantes = %s;"
                    valores = (TipoGasto, FechaComp, NumLote, NombresApellidos, Glosa, Ingreso, Egreso, Saldocaja, IdComprobantes)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Comprobante '{IdComprobantes}' se ha modificado exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El Comprobante '{IdComprobantes}' Tiene Registrado Leyes O Anticipo {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El Comprobante '{IdComprobantes}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def EliminarComprobante(page, IdComprobantes):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Comprobantes WHERE Idcomprobantes = %s;"
                    valores = (IdComprobantes,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Comprobante '{IdComprobantes}' se ha Eliminado Exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El Comprobante '{IdComprobantes}' Tiene Registrado Leyes O Anticipo {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El Comprobante '{IdComprobantes}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def conboBox_Nombre_gasto():
        try:
            # Usar 'with' para manejar la conexión de manera segura
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    # Ejecutar la consulta para obtener los nombres de los conjuntos
                    cursor.execute('select TipoGasto from TipoGasto order by IdTipoGasto desc;')
                    miResultado = cursor.fetchall()
                    
                    # Retornar los resultados como una lista de nombres
                    return [x[0] for x in miResultado]
        
        except mysql.connector.Error as error:
            print(f'Error de Mostrar Datos: {error}')
            return []

class CAnticipo:
    
    @staticmethod
    def mostrarAnticipo():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Anticipo ORDER BY NumLote DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error al mostrar anticipos: {error}'

    @staticmethod
    def IngresarAnticipo(page, NumLote, FechaAnt, Anticipo, AntLiteral):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Anticipo VALUES (NULL, %s, %s, %s, %s);"
                    valores = (NumLote, FechaAnt, Anticipo, AntLiteral)
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Ingresado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error al insertar: {error}"), open=True))

    @staticmethod
    def ModificarAnticipo(page, IdAnticipo, NumLote, FechaAnt, Anticipo, AntLiteral):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Anticipo SET
                        NumLote = %s,
                        FechaAnt = %s,
                        Anticipo = %s,
                        AntLiteral = %s
                        WHERE IdAnticipo = %s;"""
                    valores = (NumLote, FechaAnt, Anticipo, AntLiteral, IdAnticipo)
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Actualizado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error de actualización: {error}"), open=True))

    @staticmethod
    def EliminarAnticipo(page, IdAnticipo):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Anticipo WHERE IdAnticipo = %s;"
                    valores = (IdAnticipo,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Eliminado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error de eliminación: {error}"), open=True))


class BMetalurgico:
    
    @staticmethod
    def mostrarLiquidacion():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM BMetalurgico ORDER BY NombreConjunto DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarBMetalurgico(page, NombreConjunto, FechaProc, TPesoC, LeyesH2OC, TnsC, LeyesZnC, LeyesAgC, LeyesPbC, TFinosZnC, TFinosAgC, TFinosPbC, TPesoC1, LeyesH2OC1, TnsC1, LeyesZnC1, LeyesAgC1, LeyesPbC1, TFinosZnC1, TFinosAgC1, TFinosPbC1, LeyesRPbZn1, LeyesRPbAg1, LeyesRPb1, TPesoC2, LeyesH2OC2, TnsC2, LeyesZnC2, LeyesAgC2, LeyesPbC2, TFinosZnC2, TFinosAgC2, TFinosPbC2, LeyesRZn2, LeyesRZnAg2, LeyesRZnPb2, colasTns, colasZn, colasAg, colasPb, colasFinosZn, colasFinosAg, colasFinosPb, colasRZn, colasRAg, colasRPb):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """INSERT INTO BMetalurgico VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
                    valores = (NombreConjunto, FechaProc, TPesoC, LeyesH2OC, TnsC, LeyesZnC, LeyesAgC, LeyesPbC, TFinosZnC, TFinosAgC, TFinosPbC, TPesoC1, LeyesH2OC1, TnsC1, LeyesZnC1, LeyesAgC1, LeyesPbC1, TFinosZnC1, TFinosAgC1, TFinosPbC1, LeyesRPbZn1, LeyesRPbAg1, LeyesRPb1, TPesoC2, LeyesH2OC2, TnsC2, LeyesZnC2, LeyesAgC2, LeyesPbC2, TFinosZnC2, TFinosAgC2, TFinosPbC2, LeyesRZn2, LeyesRZnAg2, LeyesRZnPb2, colasTns, colasZn, colasAg, colasPb, colasFinosZn, colasFinosAg, colasFinosPb, colasRZn, colasRAg, colasRPb)
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Ingresado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error Ingreso de Datos: {error}"), open=True))

    @staticmethod
    def ModificarBMetalurgico(page, NombreConjunto, FechaProc, TPesoC, LeyesH2OC, TnsC, LeyesZnC, LeyesAgC, LeyesPbC, TFinosZnC, TFinosAgC, TFinosPbC, TPesoC1, LeyesH2OC1, TnsC1, LeyesZnC1, LeyesAgC1, LeyesPbC1, TFinosZnC1, TFinosAgC1, TFinosPbC1, LeyesRPbZn1, LeyesRPbAg1, LeyesRPb1, TPesoC2, LeyesH2OC2, TnsC2, LeyesZnC2, LeyesAgC2, LeyesPbC2, TFinosZnC2, TFinosAgC2, TFinosPbC2, LeyesRZn2, LeyesRZnAg2, LeyesRZnPb2, colasTns, colasZn, colasAg, colasPb, colasFinosZn, colasFinosAg, colasFinosPb, colasRZn, colasRAg, colasRPb):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE BMetalurgico SET 
                        FechaProc=%s, TPesoC=%s, LeyesH2OC=%s, TnsC=%s, LeyesZnC=%s, 
                        LeyesAgC=%s, LeyesPbC=%s, TFinosZnC=%s, TFinosAgC=%s, 
                        TFinosPbC=%s, TPesoC1=%s, LeyesH2OC1=%s, TnsC1=%s, 
                        LeyesZnC1=%s, LeyesAgC1=%s, LeyesPbC1=%s, TFinosZnC1=%s, 
                        TFinosAgC1=%s, TFinosPbC1=%s, LeyesRPbZn1=%s, 
                        LeyesRPbAg1=%s, LeyesRPb1=%s, TPesoC2=%s, LeyesH2OC2=%s, 
                        TnsC2=%s, LeyesZnC2=%s, LeyesAgC2=%s, LeyesPbC2=%s, 
                        TFinosZnC2=%s, TFinosAgC2=%s, TFinosPbC2=%s, 
                        LeyesRZn2=%s, LeyesRZnAg2=%s, LeyesRZnPb2=%s, 
                        colasTns=%s, colasZn=%s, colasAg=%s, colasPb=%s, 
                        colasFinosZn=%s, colasFinosAg=%s, colasFinosPb=%s, 
                        colasRZn=%s, colasRAg=%s, colasRPb=%s 
                        WHERE NombreConjunto=%s"""
                    
                    valores = (FechaProc, TPesoC, LeyesH2OC, TnsC, LeyesZnC, LeyesAgC, LeyesPbC, TFinosZnC, TFinosAgC, TFinosPbC, TPesoC1, LeyesH2OC1, TnsC1, LeyesZnC1, LeyesAgC1, LeyesPbC1, TFinosZnC1, TFinosAgC1, TFinosPbC1, LeyesRPbZn1, LeyesRPbAg1, LeyesRPb1, TPesoC2, LeyesH2OC2, TnsC2, LeyesZnC2, LeyesAgC2, LeyesPbC2, TFinosZnC2, TFinosAgC2, TFinosPbC2, LeyesRZn2, LeyesRZnAg2, LeyesRZnPb2, colasTns, colasZn, colasAg, colasPb, colasFinosZn, colasFinosAg, colasFinosPb, colasRZn, colasRAg, colasRPb, NombreConjunto)
                    
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Actualizado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error de Actualización: {error}"), open=True))

    @staticmethod
    def EliminarBMetalurgico(page, NombreConjunto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM BMetalurgico WHERE NombreConjunto = %s;"
                    valores = (NombreConjunto,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Eliminado"), open=True))
        except mysql.connector.Error as error:
            page.add(ft.SnackBar(ft.Text(f"Error de Eliminación: {error}"), open=True))


class CConjunto:
 
    @staticmethod
    def mostrarConjunto():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Conjunto ORDER BY idConjunto DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarConjunto(page, NombreConjunto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Conjunto VALUES (NULL, %s);"
                    valores = (NombreConjunto,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Conjunto '{NombreConjunto}' se ha Creado exitosamente", tipo="éxito")
                    #page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Ingresado"), open=True))
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error de Conexion {error} ", tipo="error")

    @staticmethod
    def ModificarConjunto(page, NombreConjunto, IdConjunto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "UPDATE Conjunto SET NombreConjunto = %s WHERE IdConjunto = %s;"
                    valores = (NombreConjunto, IdConjunto)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Conjunto '{NombreConjunto}' se ha modificado exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error de conexion {e}", tipo="error")

    @staticmethod
    def EliminarConjunto(page, IdConjunto,NombreConjunto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Conjunto WHERE IdConjunto = %s;"
                    valores = (IdConjunto,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NombreConjunto}' se ha Eliminado Exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El Conjunto '{NombreConjunto}' error de eliminacion {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El Conjunto '{NombreConjunto}' NOse ha Eliminado {e}", tipo="error")


class CInicial:
 
    @staticmethod
    def mostrarInicial():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Inicial ORDER BY IdInicial DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarInicial(page, NombreInicial):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Inicial VALUES (NULL, %s);"
                    valores = (NombreInicial,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Conjunto '{NombreInicial}' se ha Creado exitosamente", tipo="éxito")
                    #page.add(ft.SnackBar(ft.Text(f"{cursor.rowcount} Registro Ingresado"), open=True))
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error de Conexion {error} ", tipo="error")

    @staticmethod
    def ModificarInicial(page, NombreInicial, IdInicial):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "UPDATE Inicial SET NombreInicial = %s WHERE IdInicial = %s;"
                    valores = (NombreInicial, IdInicial)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"La Inicial '{NombreInicial}' se ha modificado exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error de conexion {e}", tipo="error")

    @staticmethod
    def EliminarInicial(page, IdInicial,NombreInicial):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Inicial WHERE IdInicial = %s;"
                    valores = (IdInicial,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"La Inicial '{NombreInicial}' se ha Eliminado Exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: La Inicial '{NombreInicial}' error de eliminacion {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: La Inicial '{NombreInicial}' NO se ha Eliminado {e}", tipo="error")


class CCotizaciones:
 
    @staticmethod
    def mostrarCotizaciones():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Cotizaciones ORDER BY Fecha DESC LIMIT 100;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarCotizaciones(page, Fecha, CotQuicenalAg, CotDiaAg, CotQuincenalPb, CotDiaPb, CotQuincenalZn, CotDiaZn, AlicuotaRMAg, AlicuotaRMPb, AlicuotaRMZn, TCSusSem, TCSusDia):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Cotizaciones VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    valores = (Fecha, CotQuicenalAg, CotDiaAg, CotQuincenalPb, CotDiaPb, CotQuincenalZn, CotDiaZn, AlicuotaRMAg, AlicuotaRMPb, AlicuotaRMZn, TCSusSem, TCSusDia)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"A la Fecha '{Fecha}' se ha Agregado exitosamente", tipo="éxito")                    
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"La '{Fecha}' ya existe Cotizaciones: {error}", tipo="error")


    @staticmethod
    def ModificarCotizaciones(page, Fecha, CotQuicenalAg, CotDiaAg, CotQuincenalPb, CotDiaPb, CotQuincenalZn, CotDiaZn, AlicuotaRMAg, AlicuotaRMPb, AlicuotaRMZn, TCSusSem, TCSusDia):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Cotizaciones SET 
                        CotQuincenalAg = %s, CotDiaAg = %s, CotQuincenalPb = %s, 
                        CotDiaPb = %s, CotQuincenalZn = %s, CotDiaZn = %s, 
                        AlicuotaRMAg = %s, AlicuotaRMPb = %s, AlicuotaRMZn = %s, 
                        TCSusSem = %s, TCSusDia = %s 
                        WHERE Fecha = %s;"""
                    valores = (CotQuicenalAg, CotDiaAg, CotQuincenalPb, CotDiaPb, CotQuincenalZn, CotDiaZn, AlicuotaRMAg, AlicuotaRMPb, AlicuotaRMZn, TCSusSem, TCSusDia, Fecha)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"La '{Fecha}' se ha actualizado Corectamente", tipo="éxito")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"Error al actualizar la cooperativa: {error}", tipo="error")

    @staticmethod
    def EliminarCotizaciones(page, Fecha):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Cotizaciones WHERE Fecha = %s;"
                    valores = (Fecha,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"La '{Fecha}' se ha eliminado exitosamente", tipo="éxito")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"error. No se elimino el registro: {error}", tipo="error")

class CLiquidacion:
 
    @staticmethod
    def mostrarLiquidacion():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Liquidacion ORDER BY NumLote DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarLiquidacion(page,NumLote, NombreConjunto, FechaLiq, LeyesAgLiq, LeyesPbLiq, LeyesZnLiq, LeyesH2OLiq, KMerma, Knh, Kh2o, Kns, KFinosAg, KFinosPb, KFinosZn, VBrutoAg, VBrutoPb, VBrutoZn, VPrecioAg, VPrecioPb, VPrecioZn, TPrecioSus, VNetoSus, VNetoBs, VRMAg, VRMPb, VRMZn, VCns, VComibol, Retenciones_Fencomin, Retenciones_Fedecomin, Retenciones_Regalias, Retenciones_Cooperativa, Retenciones_Comunidad, Retenciones_Deporte, Retenciones_Afp, VTDescuentos, VTLiquidoPagable, VTLiquidoPagable1, Numletras, TotalRm, VTRetenciones, VTLiqPag, VPrecioAgSusTon, VPrecioPbSusTon, VPrecioZnSusTon, VPrecioAgSus, VPrecioPbSus, VPrecioZnSus, VPrecioAgBs, VPrecioPbBs, VPrecioZnBs, TotalRmNeto, BonoExtra, BonoTransporte, Totalabc, VRMAgNeto, VRMPbNeto, VRMZnNeto, TotalDescuentosLey, TotalImporteFinal, LeyesAgVen, LeyesPbVen, LeyesZnVen, LabVen,NombreInicial):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    # Consulta SQL corregida
                    sql = """
                        INSERT INTO Liquidacion (
                            NumLote, NombreConjunto, FechaLiq, LeyesAgLiq, LeyesPbLiq, LeyesZnLiq, LeyesH2OLiq,
                            KMerma, Knh, Kh2o, Kns, KFinosAg, KFinosPb, KFinosZn, VBrutoAg, VBrutoPb, VBrutoZn,
                            VPrecioAg, VPrecioPb, VPrecioZn, TPrecioSus, VNetoSus, VNetoBs, VRMAg, VRMPb, VRMZn,
                            VCns, VComibol, Retenciones_Fencomin, Retenciones_Fedecomin, Retenciones_Regalias,
                            Retenciones_Cooperativa, Retenciones_Comunidad, Retenciones_Deporte, Retenciones_Afp,
                            VTDescuentos, VTLiquidoPagable, VTLiquidoPagable1, Numletras, TotalRm, VTRetenciones,
                            VTLiqPag, VPrecioAgSusTon, VPrecioPbSusTon, VPrecioZnSusTon, VPrecioAgSus, VPrecioPbSus,
                            VPrecioZnSus, VPrecioAgBs, VPrecioPbBs, VPrecioZnBs, TotalRmNeto, BonoExtra, BonoTransporte,
                            Totalabc, VRMAgNeto, VRMPbNeto, VRMZnNeto, TotalDescuentosLey, TotalImporteFinal,
                            LeyesAgVen, LeyesPbVen, LeyesZnVen, LabVen,NombreInicial
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        );
                    """
                    # Tupla de valores
                    valores = (
                        NumLote, NombreConjunto, FechaLiq, LeyesAgLiq, LeyesPbLiq, LeyesZnLiq, LeyesH2OLiq,
                        KMerma, Knh, Kh2o, Kns, KFinosAg, KFinosPb, KFinosZn, VBrutoAg, VBrutoPb, VBrutoZn,
                        VPrecioAg, VPrecioPb, VPrecioZn, TPrecioSus, VNetoSus, VNetoBs, VRMAg, VRMPb, VRMZn,
                        VCns, VComibol, Retenciones_Fencomin, Retenciones_Fedecomin, Retenciones_Regalias,
                        Retenciones_Cooperativa, Retenciones_Comunidad, Retenciones_Deporte, Retenciones_Afp,
                        VTDescuentos, VTLiquidoPagable, VTLiquidoPagable1, Numletras, TotalRm, VTRetenciones,
                        VTLiqPag, VPrecioAgSusTon, VPrecioPbSusTon, VPrecioZnSusTon, VPrecioAgSus, VPrecioPbSus,
                        VPrecioZnSus, VPrecioAgBs, VPrecioPbBs, VPrecioZnBs, TotalRmNeto, BonoExtra, BonoTransporte,
                        Totalabc, VRMAgNeto, VRMPbNeto, VRMZnNeto, TotalDescuentosLey, TotalImporteFinal,
                        LeyesAgVen, LeyesPbVen, LeyesZnVen, LabVen, NombreInicial
                    )
                    # Ejecutar la consulta
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Liquidado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {error}", tipo="error")
 
    @staticmethod
    def ModificarLiquidacion(page, NombreConjunto, FechaLiq, LeyesAgLiq, LeyesPbLiq, LeyesZnLiq, LeyesH2OLiq, KMerma, Knh, Kh2o, Kns, KFinosAg, KFinosPb, KFinosZn, VBrutoAg, VBrutoPb, VBrutoZn, VPrecioAg, VPrecioPb, VPrecioZn, TPrecioSus, VNetoSus, VNetoBs, VRMAg, VRMPb, VRMZn, VCns, VComibol, Retenciones_Fencomin, Retenciones_Fedecomin, Retenciones_Regalias, Retenciones_Cooperativa, Retenciones_Comunidad, Retenciones_Deporte, Retenciones_Afp, VTDescuentos, VTLiquidoPagable, VTLiquidoPagable1, Numletras, TotalRm, VTRetenciones, VTLiqPag, VPrecioAgSusTon, VPrecioPbSusTon, VPrecioZnSusTon, VPrecioAgSus, VPrecioPbSus, VPrecioZnSus, VPrecioAgBs, VPrecioPbBs, VPrecioZnBs, TotalRmNeto, BonoExtra, BonoTransporte, Totalabc, VRMAgNeto, VRMPbNeto, VRMZnNeto, TotalDescuentosLey, TotalImporteFinal, LeyesAgVen, LeyesPbVen, LeyesZnVen, LabVen, NombreInicial, NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Liquidacion SET
                        NombreConjunto = %s,
                        FechaLiq = %s,
                        LeyesAgLiq = %s,
                        LeyesPbLiq = %s,
                        LeyesZnLiq = %s,
                        LeyesH2OLiq = %s,
                        KMerma = %s,
                        Knh = %s,
                        Kh2o = %s,
                        Kns = %s,
                        KFinosAg = %s,
                        KFinosPb = %s,
                        KFinosZn = %s,
                        VBrutoAg = %s,
                        VBrutoPb = %s,
                        VBrutoZn = %s,
                        VPrecioAg = %s,
                        VPrecioPb = %s,
                        VPrecioZn = %s,
                        TPrecioSus = %s,
                        VNetoSus = %s,
                        VNetoBs = %s,
                        VRMAg = %s,
                        VRMPb = %s,
                        VRMZn = %s,
                        VCns = %s,
                        VComibol = %s,
                        Retenciones_Fencomin = %s,
                        Retenciones_Fedecomin = %s,
                        Retenciones_Regalias = %s,
                        Retenciones_Cooperativa = %s,
                        Retenciones_Comunidad = %s,
                        Retenciones_Deporte = %s,
                        Retenciones_Afp = %s,
                        VTDescuentos = %s,
                        VTLiquidoPagable = %s,
                        VTLiquidoPagable1 = %s,
                        NumLetras = %s,
                        TotalRm = %s,
                        VTRetenciones = %s,
                        VTLiqPag = %s,
                        VPrecioAgSusTon = %s,
                        VPrecioPbSusTon = %s,
                        VPrecioZnSusTon = %s,
                        VPrecioAgSus = %s,
                        VPrecioPbSus = %s,
                        VPrecioZnSus = %s,
                        VPrecioAgBs = %s,
                        VPrecioPbBs = %s,
                        VPrecioZnBs = %s,
                        TotalRmNeto = %s,
                        BonoExtra = %s,
                        BonoTransporte = %s,
                        Totalabc = %s,
                        VRMAgNeto = %s,
                        VRMPbNeto = %s,
                        VRMZnNeto = %s,
                        TotalDescuentosLey = %s,
                        TotalImporteFinal = %s,
                        LeyesAgVen = %s,
                        LeyesPbVen = %s,
                        LeyesZnVen = %s,
                        LabVen = %s,
                        NombreInicial = %s
                    WHERE NumLote = %s;"""                    
                    valores = (NombreConjunto, FechaLiq, LeyesAgLiq, LeyesPbLiq, LeyesZnLiq, LeyesH2OLiq, KMerma, Knh, Kh2o, Kns, KFinosAg, KFinosPb, KFinosZn, VBrutoAg, VBrutoPb, VBrutoZn,VPrecioAg, VPrecioPb, VPrecioZn, TPrecioSus, VNetoSus, VNetoBs, VRMAg, VRMPb, VRMZn, VCns, VComibol, Retenciones_Fencomin, Retenciones_Fedecomin, Retenciones_Regalias, Retenciones_Cooperativa, Retenciones_Comunidad, Retenciones_Deporte, Retenciones_Afp, VTDescuentos, VTLiquidoPagable, VTLiquidoPagable1, Numletras, TotalRm, VTRetenciones, VTLiqPag, VPrecioAgSusTon, VPrecioPbSusTon, VPrecioZnSusTon, VPrecioAgSus, VPrecioPbSus, VPrecioZnSus, VPrecioAgBs, VPrecioPbBs, VPrecioZnBs, TotalRmNeto, BonoExtra, BonoTransporte, Totalabc, VRMAgNeto, VRMPbNeto, VRMZnNeto, TotalDescuentosLey, TotalImporteFinal, LeyesAgVen, LeyesPbVen, LeyesZnVen, LabVen, NombreInicial, NumLote)                   
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Lote '{NumLote}' se ha modificado exitosamente", tipo="éxito")

        except Exception as e:
            mostrar_mensaje(page,f"Error: El lote '{NumLote}' Tiene Registrado Leyes O Anticipo {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El lote '{NumLote}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def EliminarLiquidacion(page, NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Liquidacion WHERE NumLote = %s;"
                    valores = (NumLote,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Eliminado Exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El lote '{NumLote}' error de eliminacion {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El lote '{NumLote}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def conboBox_NombreConjunto():
        try:
            # Usar 'with' para manejar la conexión de manera segura
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    # Ejecutar la consulta para obtener los nombres de los conjuntos
                    cursor.execute('SELECT NombreConjunto FROM Conjunto ORDER BY NombreConjunto DESC;')
                    miResultado = cursor.fetchall()
                    
                    # Retornar los resultados como una lista de nombres
                    return [x[0] for x in miResultado]
        
        except mysql.connector.Error as error:
            print(f'Error de Mostrar Datos: {error}')
            return []
        
    @staticmethod
    def conboBox_NombreInicial():
        try:
            # Usar 'with' para manejar la conexión de manera segura
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    # Ejecutar la consulta para obtener los nombres de los conjuntos
                    cursor.execute('SELECT NombreInicial FROM Inicial ORDER BY NombreInicial DESC;')
                    miResultado_inicial = cursor.fetchall()
                    
                    # Retornar los resultados como una lista de nombres
                    return [x[0] for x in miResultado_inicial]
        
        except mysql.connector.Error as error:
            print(f'Error de Mostrar Datos: {error}')
            return []    

class CProveedores:
 
    @staticmethod
    def mostrarProveedores():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Proveedores ORDER BY NombresApellidos ASC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarProveedores(page, NombresApellidos, CarnetIdentidad, Denominacion):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Proveedores VALUES (NULL, %s, %s, %s);"
                    valores = (NombresApellidos, CarnetIdentidad, Denominacion)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' se ha creado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' ya existe: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' ya existe: {error}", tipo="error")

    @staticmethod
    def ModificarProveedores(page, NombresApellidos, CarnetIdentidad, Denominacion, IdProveedores):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "UPDATE Proveedores SET NombresApellidos = %s, CarnetIdentidad = %s, Denominacion = %s WHERE IdProveedores = %s;"
                    valores = (NombresApellidos, CarnetIdentidad, Denominacion, IdProveedores)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' se ha actualizado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' Tiene Lotes: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' Tiene Lotes: {error}", tipo="error")

    @staticmethod
    def EliminarProveedores(page, IdProveedores,NombresApellidos):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Proveedores WHERE IdProveedores = %s;"
                    valores = (IdProveedores,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' se ha creado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' Tiene Lotes: {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"El Cliente '{NombresApellidos}' Tiene Lotes: {error}", tipo="error")

    @staticmethod
    def buscarnombresapellidos(nombres):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "SELECT * FROM proveedores WHERE nombresapellidos = %s;"
                    cursor.execute(sql, (nombres,))
                    return cursor.fetchone()
        
        except mysql.connector.Error as error:
            return f'Error al buscar lote: {error}'


class CRecepcion:
 
    @staticmethod
    def mostrarRecepcion():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Recepcion ORDER BY NumLote DESC LIMIT 100 ;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'
        
    @staticmethod
    def buscar_numero_recepcion(NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "SELECT * FROM recepcion WHERE NumLote = %s;"
                    cursor.execute(sql, (NumLote,))
                    return cursor.fetchone()
        
        except mysql.connector.Error as error:
            return f'Error al buscar lote: {error}'    

    @staticmethod
    def IngresarRecepcion(page, NumLote, Fecha, NombresApellidos, CarnetIdentidad, Denominacion, Municipio, NumeroOrden, Procedencia, Formulario_101, Concesion, Peso, Estado):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO Recepcion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    valores = (NumLote, Fecha, NombresApellidos, CarnetIdentidad, Denominacion, Municipio, NumeroOrden, Procedencia, Formulario_101, Concesion, Peso, Estado)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Recepcionado exitosamente", tipo="éxito")
        except ValueError as e:
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {error}", tipo="error")

    @staticmethod
    def ModificarRecepcion(page, NumLote, Fecha, NombresApellidos, CarnetIdentidad, Denominacion, Municipio, NumeroOrden, Procedencia, Formulario_101, Concesion, Peso, Estado):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Recepcion SET 
                        Fecha = %s, 
                        NombresApellidos = %s, 
                        CarnetIdentidad = %s, 
                        Denominacion = %s, 
                        Municipio = %s, 
                        NumeroOrden = %s, 
                        Procedencia = %s, 
                        Formulario_101 = %s, 
                        Concesion = %s, 
                        Peso = %s, 
                        Estado = %s 
                    WHERE NumLote = %s;"""
                    valores = (Fecha, NombresApellidos, CarnetIdentidad, Denominacion, Municipio, NumeroOrden, Procedencia, Formulario_101, Concesion, Peso, Estado, NumLote)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Actualizado exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El lote '{NumLote}' Tiene Registrado Leyes O Anticipo {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El lote '{NumLote}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def EliminarRecepcion(page, NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Recepcion WHERE NumLote = %s;"
                    valores = (NumLote,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Eliminado Exitosamente", tipo="éxito")
        except Exception as e:
            mostrar_mensaje(page,f"Error: El lote '{NumLote}' Tiene Registrado Leyes O Anticipo {e}", tipo="error")
        except mysql.connector.Error as e:
            mostrar_mensaje(page, f"Error: El lote '{NumLote}' NO se ha Eliminado {e}", tipo="error")

    @staticmethod
    def obtenerNombres():
        try:
            with CConection.ConexionBasedeDatos() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT DISTINCT NombresApellidos FROM Proveedores ORDER BY NombresApellidos")
                    nombres = cursor.fetchall()
                    return [nombre[0] for nombre in nombres]
        except mysql.connector.Error as e:
            print(f'Error al obtener los nombres: {e}')
            return []
        except Exception as e:
            print(f'Error inesperado: {e}')
            return []

    @staticmethod
    def actualizarNombresApellidos(antiguo_nombre, nuevo_nombre):
        try:
            with CConection.ConexionBasedeDatos() as conexion:
                with conexion.cursor() as cursor:
                    # Iniciar transacción
                    conexion.start_transaction()
                    
                    try:
                        # Desactivar restricciones de clave externa
                        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

                        # Actualizar en Proveedores
                        cursor.execute("""
                            UPDATE Proveedores
                            SET NombresApellidos = %s
                            WHERE NombresApellidos = %s
                        """, (nuevo_nombre, antiguo_nombre))

                        # Actualizar en Recepcion
                        cursor.execute("""
                            UPDATE Recepcion
                            SET NombresApellidos = %s
                            WHERE NombresApellidos = %s
                        """, (nuevo_nombre, antiguo_nombre))

                        # Reactivar restricciones
                        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

                        # Confirmar cambios
                        conexion.commit()
                        return True

                    except Exception as e:
                        # Revertir en caso de error
                        conexion.rollback()
                        raise e

        except mysql.connector.Error as e:
            print(f'Error de base de datos: {e}')
            return f"Error al actualizar: {e}"
        except Exception as e:
            print(f'Error inesperado: {e}')
            return f"Error inesperado: {e}"

    @staticmethod
    def obtenerUsuarios():
        try:
            with CConection.ConexionBasedeDatos() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT username FROM users ORDER BY username")
                    usuarios = cursor.fetchall()
                    return [usuario[0] for usuario in usuarios]
        except mysql.connector.Error as e:
            print(f'Error de base de datos: {e}')
            return []
        except Exception as e:
            print(f'Error inesperado: {e}')
            return []

class CTipoGasto:
 
    @staticmethod
    def mostrarTipoGasto():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM TipoGasto ORDER BY idtipogasto DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarTipoGasto(page, TipoGasto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO TipoGasto VALUES (NULL, %s);"
                    valores = (TipoGasto,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Numero Tipo de Gasto se ha Creado exitosamente", tipo="éxito")
        except ValueError as e:
            mostrar_mensaje(page, f"Error: {e}", tipo="error")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"Error: {error}", tipo="error")

    @staticmethod
    def ModificarTipoGasto(page, TipoGasto, IdTipoGasto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "UPDATE TipoGasto SET TipoGasto = %s WHERE IdTipoGasto = %s;"
                    valores = (TipoGasto, IdTipoGasto)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Numero Tipo de Gasto '{IdTipoGasto}' se ha modificado exitosamente", tipo="éxito")
        except ValueError as e:
            mostrar_mensaje(page, f"Error: {e}", tipo="error")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"Error: {error}", tipo="error")

    @staticmethod
    def EliminarTipoGasto(page, IdTipoGasto):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM TipoGasto WHERE IdTipoGasto = %s;"
                    valores = (IdTipoGasto,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El Numero Tipo de Gasto '{IdTipoGasto}' se ha eliminado exitosamente", tipo="éxito")
        except ValueError as e:
            mostrar_mensaje(page, f"Error: {e}", tipo="error")
        except mysql.connector.Error as error:
            mostrar_mensaje(page, f"Error: {error}", tipo="error")


class CTransporte:
 
    @staticmethod
    def mostrarAnticipoTrans():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM transporte ORDER BY NumLote DESC;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error de Mostrar Datos: {error}'

    @staticmethod
    def IngresarAnticipoTrans(page, NumLote, FechaAntTrans, Anticipo1, AntLiteral1):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "INSERT INTO transporte VALUES (NULL, %s, %s, %s, %s);"
                    valores = (NumLote, FechaAntTrans, Anticipo1, AntLiteral1)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Ingresado exitosamente el Anticipo", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote: '{NumLote}' {error}", tipo="error")

    @staticmethod
    def ModificarAnticipoTrans(page, NumLote, FechaAntTrans, Anticipo1, AntLiteral1, IdTransporte):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """
                    UPDATE transporte 
                    SET NumLote = %s, FechaAntTrans = %s, Anticipo1 = %s, AntLiteral1 = %s 
                    WHERE IdTransporte = %s;
                    """
                    valores = (NumLote, FechaAntTrans, Anticipo1, AntLiteral1, IdTransporte)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Actualizado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote: '{NumLote}' {error}", tipo="error")

    @staticmethod
    def EliminarAnticipoTrans(page, IdTransporte,NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM transporte WHERE IdTransporte = %s;"
                    valores = (IdTransporte,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Eliminado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote: '{NumLote}' {error}", tipo="error")

    @staticmethod
    def buscarLotetransporte(num_lote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "SELECT * FROM transporte WHERE NumLote = %s;"
                    cursor.execute(sql, (num_lote,))
                    return cursor.fetchone()
        
        except mysql.connector.Error as error:
            return f'Error al buscar lote: {error}'

class CLeyes:
    
    @staticmethod
    def mostrarLeyes():
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    cursor.execute('SELECT * FROM Leyes ORDER BY NumLote DESC LIMIT 10 ;')
                    return cursor.fetchall()
        except mysql.connector.Error as error:
            return f'Error al mostrar datos: {error}'

    @staticmethod
    def IngresarLeyes(page, NumLote, NombreLaboratorio, NumCertificado, LeyesAg, LeyesPb, LeyesZn, LeyesH2O):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = sql = """INSERT INTO Leyes VALUES (
                        NULL, %s, %s, %s, %s, %s, %s, %s
                    )""" 
                    valores = (NumLote, NombreLaboratorio, NumCertificado, LeyesAg, LeyesPb, LeyesZn, LeyesH2O)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Ingresado exitosamente la Leyes", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {error}", tipo="error")

    @staticmethod
    def ModificarLeyes(page, IdLeyes, NumLote, NombreLaboratorio, NumCertificado, LeyesAg, LeyesPb, LeyesZn, LeyesH2O):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = """UPDATE Leyes SET
                        NumLote = %s,
                        NombreLaboratorio = %s,
                        NumCertificado = %s,
                        LeyesAg = %s,
                        LeyesPb = %s,
                        LeyesZn = %s,
                        LeyesH2O = %s
                        WHERE IdLeyes = %s;"""
                    valores = (NumLote, NombreLaboratorio, NumCertificado, LeyesAg, LeyesPb, LeyesZn, LeyesH2O, IdLeyes)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Actualizado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {error}", tipo="error")

    @staticmethod
    def EliminarLeyes(page, IdLeyes,NumLote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "DELETE FROM Leyes WHERE IdLeyes = %s;"
                    valores = (IdLeyes,)
                    cursor.execute(sql, valores)
                    cone.commit()
                    mostrar_mensaje(page, f"El lote '{NumLote}' se ha Eliminado exitosamente", tipo="éxito")
        except ValueError as e:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {e}", tipo="error")
        except mysql.connector.Error as error:
            # Mostrar mensaje de error
            mostrar_mensaje(page, f"Error El lote '{NumLote}' {error}", tipo="error")

    @staticmethod
    def buscarLote(num_lote):
        try:
            with CConection.ConexionBasedeDatos() as cone:
                with cone.cursor() as cursor:
                    sql = "SELECT * FROM Leyes WHERE NumLote = %s;"
                    cursor.execute(sql, (num_lote,))
                    return cursor.fetchone()
        
        except mysql.connector.Error as error:
            return f'Error al buscar lote: {error}'
