def juego_tabla_multiplicar():
    # 1. Validación del número (1 al 100)
    while True:
        try:
            numero = int(input("Ingresa un número del 1 al 100: "))
            if 1 <= numero <= 100:
                break
            print("❌ El número debe estar entre 1 y 100.")
        except ValueError:
            print("❌ Ingresa un número entero válido.")

    # 2. Selección de modo
    print("\n¿Qué deseas hacer?")
    print("1. Ver la tabla de multiplicar")
    print("2. Responder la tabla (Examen interactivo)")
    
    while True:
        opcion = input("Elige una opción (1 o 2): ").strip()
        if opcion in ["1", "2"]:
            break
        print("❌ Opción no válida. Escribe 1 o 2.")

    # Opción 1: Mostrar la tabla
    if opcion == "1":
        print(f"\n--- TABLA DEL {numero} ---")
        for i in range(1, 11):
            print(f"{numero} x {i:2d} = {numero * i}")

    # Opción 2: Juego de preguntas
    else:
        print(f"\n--- EXAMEN DE LA TABLA DEL {numero} ---")
        aciertos = 0

        for i in range(1, 11):
            respuesta_correcta = numero * i
            
            while True:
                try:
                    respuesta_usuario = int(input(f"¿Cuánto es {numero} x {i}? "))
                    break
                except ValueError:
                    print("Por favor, ingresa una respuesta numérica.")

            if respuesta_usuario == respuesta_correcta:
                print("¡Correcto! ✨\n")
                aciertos += 1
            else:
                print(f"Incorrecto. La respuesta era {respuesta_correcta}.\n")

        # Resultado final
        print("=" * 35)
        print(f"Resultado final: {aciertos}/10 aciertos")
        if aciertos == 10:
            print("¡Perfecto! Dominas esta tabla al 100%. 🏆")
        elif aciertos >= 7:
            print("¡Buen trabajo! Tienes una buena base. 👍")
        else:
            print("Sigue practicando para mejorar. 💪")

# Para ejecutar la función:
juego_tabla_multiplicar()