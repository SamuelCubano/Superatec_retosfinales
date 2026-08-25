# Ejercicio 28: Genera los primeros 10 números de la serie de Fibonacci (0, 1, 1, 2, 3, 5...).

def generar_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]

    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie

# Generar e imprimir los primeros 10 numeros
limite = 10
fibonacci_10 = generar_fibonacci(limite)

print("--- SERIE DE FIBONACCI ---")
print(f"Primeros {limite} numeros:")
print(fibonacci_10)

# Impresion formateada
print("\nFormato secuencia:")
print(" -> ".join(map(str, fibonacci_10)))