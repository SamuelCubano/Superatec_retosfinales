# Ejercicio 30: Juego de adivinar un número del 1 al 50 (definido en una variable): dale pistas al usuario de "mayor" o "menor" hasta que acierte.

def juego_adivinanza():
    NUMERO_SECRETO = 34  # Numero a adivinar entre 1 y 50
    intentos = 0
    acertado = False

    print("--- JUEGO DE ADIVINANZA (1 al 50) ---")

    while not acertado:
        try:
            intento = int(input("Ingresa tu numero: "))
            intentos += 1

            if intento < 1 or intento > 50:
                print("Por favor, ingresa un numero dentro del rango (1 a 50).\n")
                continue

            if intento < NUMERO_SECRETO:
                print("El numero es MAYOR.\n")
            elif intento > NUMERO_SECRETO:
                print("El numero es MENOR.\n")
            else:
                acertado = True
                print("\n--- ¡ACERTASTE! ---")
                print(f"El numero era {NUMERO_SECRETO}.")
                print(f"Numero total de intentos: {intentos}")

        except ValueError:
            print("Error: Ingresa un numero entero valido.\n")

juego_adivinanza()