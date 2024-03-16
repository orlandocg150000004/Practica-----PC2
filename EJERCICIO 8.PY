def factorial(numero):
    # Verificar si el número es negativo
    if numero < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    
    # Inicializar el resultado como 1
    resultado = 1
    
    # Calcular el factorial
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado

# Ejemplos de uso:
print(factorial(5))  # Salida: 120 (5! = 5*4*3*2*1 = 120)
print(factorial(0))  # Salida: 1 (0! = 1)
print(factorial(10)) # Salida: 3628800 (10! = 10*9*8*7*6*5*4*3*2*1 = 3628800)