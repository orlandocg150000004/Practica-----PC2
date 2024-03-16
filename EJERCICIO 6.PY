def fibonacci_hasta_50():
    fibonacci = [0, 1]
    while True:
        siguiente = fibonacci[-1] + fibonacci[-2]
        if siguiente >= 50:
            break
        fibonacci.append(siguiente)
    return fibonacci

# Obtener la serie de Fibonacci hasta 50
serie_fibonacci = fibonacci_hasta_50()

# Mostrar la serie de Fibonacci
print("Serie de Fibonacci hasta el número más cercano a 50:")
print(serie_fibonacci)