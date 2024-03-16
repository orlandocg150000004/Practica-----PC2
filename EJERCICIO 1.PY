def encontrar_numeros_divisibles():
    numeros_divisibles = []
    for numero in range(1500, 2701):
        if numero % 7 == 0 and numero % 5 == 0:
            numeros_divisibles.append(numero)
    return numeros_divisibles

# Iterar sobre los números en el rango y encontrar los divisibles
numeros_divisibles = encontrar_numeros_divisibles()

# Mostrar los números encontrados
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
for numero in numeros_divisibles:
    print(numero)