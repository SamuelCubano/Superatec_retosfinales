#Cuenta la frecuencia de cada letra en una palabra usando un diccionario.

def contar_frecuencia_letras(palabra):
    palabra = palabra.lower()
    
    frecuencia = {}
    
    for letra in palabra:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
            
    return frecuencia


texto = input("ingrese una palabra: ")
resultado = contar_frecuencia_letras(texto)

print(resultado)