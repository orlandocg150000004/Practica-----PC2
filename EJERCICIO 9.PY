def omitir_vocales(cadena):
    vocales = "AEIOUaeiou"
    cadena_sin_vocales = ""
    for caracter in cadena:
        if caracter not in vocales:
            cadena_sin_vocales += caracter
    return cadena_sin_vocales

# Ejemplo de uso:
texto = input("Ingrese una cadena de texto: ")
texto_sin_vocales = omitir_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)