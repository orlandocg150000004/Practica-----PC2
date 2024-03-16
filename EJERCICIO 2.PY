# Definir el número de filas del patrón
num_filas = 5

# Construir la parte superior del patrón
for i in range(num_filas):
    print("* " * (i + 1))

# Construir la parte inferior del patrón
for i in range(num_filas - 1, 0, -1):
    print("* " * i)