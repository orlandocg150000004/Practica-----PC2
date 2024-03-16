numeros = []

# Permitir al usuario ingresar números hasta que decida no ingresar más
while True:
    respuesta = input("Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta.upper() == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, responda SI o NO.")

# Contar la cantidad de números pares e impares
pares = 0
impares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)