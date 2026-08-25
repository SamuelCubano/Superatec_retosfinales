def invertir_frase_bucle(frase):
    frase_invertida = ""
    for caracter in frase:
        frase_invertida = caracter + frase_invertida
    return frase_invertida

# Ejemplo de uso interactivo:
texto_usuario = input("Escribe una frase: ")
resultado = invertir_frase_bucle(texto_usuario)

print(f"Frase invertida: {resultado}")