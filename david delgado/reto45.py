# Pedir la frase al usuario
frase = input("Introduce una frase: ")

# Definir las vocales (incluyendo mayúsculas y acentuadas)
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Contar cuántas vocales hay en la frase
contador_vocales = sum(1 for caracter in frase if caracter in vocales)

print(f"La frase contiene {contador_vocales} vocal(es).")