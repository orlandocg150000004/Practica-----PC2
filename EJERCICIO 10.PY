def convertir_a_formato_texto(fecha):
    partes_fecha = fecha.split("-")
    año = partes_fecha[0]
    mes = int(partes_fecha[1])
    dia = int(partes_fecha[2])
    
    # Definir una lista de nombres de meses
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Obtener el nombre del mes
    nombre_mes = nombres_meses[mes - 1]
    
    # Formatear la fecha en el formato deseado
    fecha_formateada = f"{nombre_mes} {dia}, {año}"
    
    return fecha_formateada

# Ejemplo de uso:
fecha = "1970-01-01"
print("Input:", fecha, "| Output:", convertir_a_formato_texto(fecha))