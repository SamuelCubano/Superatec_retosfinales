#Crea una lista de compras: permite agregar productos hasta que el usuario escriba "fin", luego muestra la lista numerada.

def crear_lista_compras():
    compras = []
    print("--- Creador de Lista de Compras ---")
    print("Escribe los productos que deseas agregar. Escribe 'fin' para terminar.\n")
    
    while True:
        producto = input("Añadir producto: ").strip()
        
        # Condición para salir del bucle (ignorando mayúsculas/minúsculas)
        if producto.lower() == 'fin':
            break
            
        # Validamos que no se agreguen entradas vacías
        if producto:
            compras.append(producto)
        else:
            print("Por favor, introduce un nombre de producto válido.")
            
    # Si la lista tiene elementos, los mostramos numerados
    if compras:
        print("\n--- Tu Lista de Compras ---")
        # Usamos enumerate() para obtener el índice y el producto (empezando en 1)
        for i, item in enumerate(compras, start=1):
            print(f"{i}. {item}")
    else:
        print("\nLa lista de compras está vacía.")

# Ejecutamos la función
crear_lista_compras()