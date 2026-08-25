def imprimir_pares(limite=50):
    print(f"\n--- Números pares del 1 al {limite} ---")
    for numero in range(2, limite + 1, 2):
        print(numero, end=" ")
    print()  # Salto de línea final

# 1. Uso por defecto (del 1 al 50)
imprimir_pares()

# 2. Uso interactivo especificando el límite
try:
    entrada = input("\nIngresa hasta qué número deseas imprimir los pares (presiona Enter para salir): ").strip()
    if entrada:
        limite_usuario = int(entrada)
        imprimir_pares(limite_usuario)
except ValueError:
    print("❌ Por favor ingresa un número entero válido.")