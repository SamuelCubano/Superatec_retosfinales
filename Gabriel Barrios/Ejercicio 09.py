# Ejercicio 09: Pide tu año de nacimiento y calcula qué edad tendrás este año.

from datetime import datetime

def calcular_edad():
    try:
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
        año_actual = datetime.now().year
        
        edad = año_actual - año_nacimiento
        
        print("\n--- RESUMEN DE EDAD ---")
        print(f"Año de nacimiento: {año_nacimiento}")
        print(f"Año actual:        {año_actual}")
        print(f"Edad este año:     {edad} años")

    except ValueError:
        print("Error: Por favor, ingrese un año valido (numero entero).")

calcular_edad()