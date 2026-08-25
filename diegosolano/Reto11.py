def evaluar_numero(numero):
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

# Ejemplo de uso interactivo:
entrada = float(input("Ingresa un número: "))
resultado = evaluar_numero(entrada)

print(resultado)