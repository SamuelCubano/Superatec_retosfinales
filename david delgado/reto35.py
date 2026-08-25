# Lista de ejemplo
numeros = [14, 52, 8, 99, 3, 73, 21]

# Asumimos inicialmente que el primer número es el mayor
mayor = numeros[0]

# Recorremos la lista para comparar cada elemento
for num in numeros:
    if num > mayor:
        mayor = num

print(f"El número más grande de la lista es: {mayor}")