from decimal import Decimal

def num_letras(valor, moneda_singular="", moneda_plural=""):
    valor = Decimal(valor)
    # Tomamos el valor absoluto para ignorar el signo negativo
    valor_abs = abs(valor)
    cantidad = int(valor_abs)
    centavos = int((valor_abs - Decimal(cantidad)) * 100)
    valor_entero = cantidad

    if valor_abs == Decimal('0.00'):
        return "SON: CERO 00/100 BOLIVIANOS"

    unidades = ["UN", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE", "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIESISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE", "VEINTE", "VEINTIUNO", "VEINTIDOS", "VEINTITRES", "VEINTICUATRO", "VEINTICINCO", "VEINTISEIS", "VEINTISIETE", "VEINTIOCHO", "VEINTINUEVE"]
    decenas = ["DIEZ", "VEINTI", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    centenas = ["CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]

    numero_bloques = 1
    bloque = ""
    bloque_cero = 0

    while cantidad > 0:
        primer_digito = 0
        segundo_digito = 0
        tercer_digito = 0
        bloque = ""

        for i in range(3):
            digito = cantidad % 10
            if digito != 0:
                if i == 0:
                    bloque = " " + unidades[digito - 1]
                    primer_digito = digito
                elif i == 1:
                    if digito <= 2:
                        bloque = " " + unidades[(digito * 10) + primer_digito - 1]
                    else:
                        bloque = " " + decenas[digito - 1] + (" Y" if primer_digito != 0 else "") + bloque
                    segundo_digito = digito
                elif i == 2:
                    bloque = " " + (centenas[digito - 1] if digito != 1 or primer_digito != 0 or segundo_digito != 0 else "CIEN") + bloque
                    tercer_digito = digito
            else:
                bloque_cero += 1

            cantidad //= 10
            if cantidad == 0:
                break

        if numero_bloques == 1:
            num_letras = bloque
        elif numero_bloques == 2:
            if bloque.strip() == "UN":
                num_letras = "UN MIL " + num_letras
            else:
                num_letras = bloque + " MIL " + num_letras
        elif numero_bloques == 3:
            if bloque.strip() == "UN":
                num_letras = "UN MILLON " + num_letras
            else:
                num_letras = bloque + " MILLONES " + num_letras

        numero_bloques += 1

    # Agregamos "MENOS " al principio si el valor original era negativo
    prefijo = "MENOS " if valor < 0 else ""
    num_letras = "SON: " + prefijo + num_letras + " " + str(centavos).zfill(2) + "/100 BOLIVIANOS" + (" " + moneda_singular if valor_entero == 1 else " " + moneda_plural)
    return num_letras