def contar_digitos(numero, digito):
    numero_str = str(numero)
    return numero_str.count(str(digito))

# Solicitar al usuario el número y el dígito
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito a contar: "))

# Contar la cantidad de veces que aparece el dígito en el número
cantidad = contar_digitos(numero, digito)

# Mostrar el resultado
print(f"Cantidad de veces {digito} en el número: {cantidad}")
