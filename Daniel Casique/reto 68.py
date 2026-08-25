#Traductor simple: diccionario español-inglés con 5 palabras. El usuario escribe una palabra y recibe su traducción (o "no existe").

def traductor_simple():
    # Diccionario con 5 palabras español-inglés
    diccionario = {
        "perro": "dog",
        "gato": "cat",
        "casa": "house",
        "libro": "book",
        "agua": "water"
    }
    
    # Solicitamos la palabra al usuario y la convertimos a minúsculas para evitar errores
    palabra = input("Introduce una palabra en español para traducir: ").strip().lower()
    
    # Buscamos la palabra en el diccionario
    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es: **{diccionario[palabra]}**")
    else:
        print("No existe")

# Ejecutamos la función
traductor_simple()