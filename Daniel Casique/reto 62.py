#Crea una función es_bisiesto(anio) que diga si un año es bisiesto (divisible entre 4, excepto los divisibles entre 100 salvo que también sean divisibles entre 400).

def es_bisiesto(anio):
    # Un año es bisiesto si:
    # 1. Es divisible entre 4 Y NO es divisible entre 100, O
    # 2. Es divisible entre 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

    if true:
        print("es bisiesto")

# Ejemplos de uso:
print(es_bisiesto(2024))  # Salida: True (Es divisible por 4 y no por 100)
print(es_bisiesto(1900))  # Salida: False (Es divisible por 4 y por 100, pero no por 400)
print(es_bisiesto(2000))  # Salida: True (Es divisible por 400)
print(es_bisiesto(2023))  # Salida: False (No es divisible por 4)