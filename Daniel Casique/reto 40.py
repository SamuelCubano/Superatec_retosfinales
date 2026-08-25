#Pide las notas de un curso y muestra: promedio, nota más alta y nota más baja.

def gestionar_notas():
    notas = []
    print("Introduce las notas del curso (escribe 'fin' para terminar):")
    
    while True:
        entrada = input("Nota: ")
        
        # Condición para salir del bucle
        if entrada.lower() == 'fin':
            break
            
        try:
            nota = float(entrada)
            # Validamos que la nota esté en un rango lógico (ej. 0 a 10 o 0 a 100)
            if nota < 0:
                print("La nota no puede ser negativa. Inténtalo de nuevo.")
                continue
            notas.append(nota)
        except ValueError:
            print("Por favor, introduce un número válido o 'fin'.")
            
    # Si la lista está vacía, evitamos errores al calcular
    if not notas:
        print("\nNo se registraron notas.")
        return
        
    # Cálculos principales
    promedio = sum(notas) / len(notas)
    nota_alta = max(notas)
    nota_baja = min(notas)
    
    # Resultados
    print("\n--- Resultados del Curso ---")
    print(f"Total de notas ingresadas: {len(notas)}")
    print(f"Promedio: **{promedio:.2f}**")
    print(f"Nota más alta: **{nota_alta}**")
    print(f"Nota más baja: **{nota_baja}**")

# Ejecutamos la función
gestionar_notas()