# Ejercicio 10: Intercambia los valores de dos variables e imprímelas antes y después del intercambio.

def intercambiar_variables():
    # Asignacion inicial de valores
    a = 15
    b = 42

    print("--- ANTES DEL INTERCAMBIO ---")
    print(f"Variable A: {a}")
    print(f"Variable B: {b}")

    # Intercambio idiomático de Python (desempaquetado de tuplas)
    a, b = b, a

    print("\n--- DESPUES DEL INTERCAMBIO ---")
    print(f"Variable A: {a}")
    print(f"Variable B: {b}")

intercambiar_variables()