#Crea una función es_bisiesto(anio) que diga si un año es bisiesto (divisible entre 4, excepto los divisibles entre 100 salvo que también sean divisibles entre 400).

def verificar_bisiesto(anio):
    # Verificamos si es bisiesto con la regla lógica
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} **sí es bisiesto**.")
    else:
        print(f"El año {anio} **no es bisiesto**.")

# Ejemplos de uso:
verificar_bisiesto(2024)  # Salida: El año 2024 sí es bisiesto.
verificar_bisiesto(1900)  # Salida: El año 1900 no es bisiesto.
verificar_bisiesto(2000)  # Salida: El año 2000 sí es bisiesto.
verificar_bisiesto(2023)  # Salida: El año 2023 no es bisiesto.