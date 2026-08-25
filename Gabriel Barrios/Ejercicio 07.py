# Ejercicio 07: Pide cuántos kilómetros recorriste y muestra cuántos metros y centímetros son.

def convertir_distancia():
    try:
        km = float(input("Ingrese los kilómetros recorridos: "))

        metros = km * 1000
        centimetros = km * 100_000

        print("\n--- RESULTADO DE CONVERSIÓN ---")
        print(f" Distancia:     {km:,.2f} km".replace(",", " "))
        print(f" Metros:        {metros:,.2f} m".replace(",", " "))
        print(f" Centímetros:   {centimetros:,.2f} cm".replace(",", " "))

    except ValueError:
        print(" Error: Por favor, ingrese un número válido.")

convertir_distancia()