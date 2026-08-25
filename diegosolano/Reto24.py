def sumar_hasta_numero():
    # Validación para asegurar que sea un número entero positivo
    while True:
        try:
            limite = int(input("Ingresa un número entero positivo: "))
            if limite >= 1:
                break
            print("❌ El número debe ser mayor o igual a 1.")
        except ValueError:
            print("❌ Entrada no válida. Ingresa un número entero.")

    # Opción 1: Usando la función sum() con range()
    suma_total = sum(range(1, limite + 1))

    # Imprimir el resultado
    print(f"\n👉 La suma de todos los números del 1 al {limite} es: {suma_total}")

# Para ejecutar la función:
sumar_hasta_numero()