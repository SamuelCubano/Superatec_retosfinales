def quiz_interactivo():
    # Estructura de datos para los cuestionarios, preguntas y niveles
    quizzes = {
        "1": {
            "titulo": "Cultura General de Venezuela",
            "preguntas": [
                {
                    "pregunta": "¿Cuál es la caída de agua más alta del mundo ubicada en Venezuela?",
                    "opciones": ["1) Salto del Ángel", "2) Cataratas del Iguazú", "3) Salto Kukenán"],
                    "correcta": 1
                },
                {
                    "pregunta": "¿En qué estado ocurre el Relámpago del Catatumbo?",
                    "opciones": ["1) Falcón", "2) Zulia", "3) Mérida"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Cuál es la capital del estado Lara?",
                    "opciones": ["1) Valencia", "2) Barquisimeto", "3) Maracay"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Qué plato tradicional lleva carne desmechada, arroz, caraotas y tajadas?",
                    "opciones": ["1) Hallaca", "2) Pabellón Criollo", "3) Asado Negro"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Quién escribió la novela 'Doña Bárbara'?",
                    "opciones": ["1) Rómulo Gallegos", "2) Andrés Eloy Blanco", "3) Arturo Uslar Pietri"],
                    "correcta": 1
                }
            ],
            "niveles": [
                (0, 20, "Turista Despistado 🗺️", "¡Apenas estás empezando a conocer la cultura venezolana!"),
                (40, 60, "Conocedor Criollo 🥑", "¡Tienes muy buen conocimiento sobre las tradiciones y geografía!"),
                (80, 100, "Ilustre Ilustrado 📜", "¡Eres todo un experto en cultura general venezolana! ¡Patria, llano y saber!")
            ]
        },
        "2": {
            "titulo": "My Hero Academia",
            "preguntas": [
                {
                    "pregunta": "¿Cuál es el nombre del Don (Quirk) original de All Might y Deku?",
                    "opciones": ["1) Explosión", "2) One For All", "3) All For One"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Cómo se llama el héroe profesional N° 1 antes del retiro de All Might?",
                    "opciones": ["1) Endeavor", "2) All Might", "3) Hawks"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Cuál es el nombre verdadero de Deku?",
                    "opciones": ["1) Katsuki Bakugo", "2) Izuku Midoriya", "3) Shoto Todoroki"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿En qué academia prestigiosa estudian los protagonistas?",
                    "opciones": ["1) Academia U.A.", "2) Academia Shiketsu", "3) Instituto Isamu"],
                    "correcta": 1
                },
                {
                    "pregunta": "¿Cuál es el nombre de villano del líder de la Liga de Villanos?",
                    "opciones": ["1) Dabi", "2) Tomura Shigaraki", "3) Overhaul"],
                    "correcta": 2
                }
            ],
            "niveles": [
                (0, 20, "Héroe Novato 🐣", "Aún estás en la clase de prueba. ¡Sigue entrenando duro!"),
                (40, 60, "Estudiante de la U.A. 🎒", "¡Has superado el examen de admisión! Vas camino a ser un profesional."),
                (80, 100, "Héroe Profesional N° 1 🦸‍♂️", "¡PLUS ULTRA! Tu conocimiento rivaliza con los más grandes héroes.")
            ]
        },
        "3": {
            "titulo": "Programación en Python",
            "preguntas": [
                {
                    "pregunta": "¿Cuál es la sintaxis correcta para imprimir en pantalla en Python 3?",
                    "opciones": ["1) print('Hola')", "2) echo 'Hola'", "3) Console.WriteLine('Hola')"],
                    "correcta": 1
                },
                {
                    "pregunta": "¿Qué tipo de dato devuelve `type([1, 2, 3])`?",
                    "opciones": ["1) tuple", "2) dict", "3) list"],
                    "correcta": 3
                },
                {
                    "pregunta": "¿Qué símbolo se utiliza para comentarios de una sola línea?",
                    "opciones": ["1) //", "2) #", "3) /*"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Qué palabra clave se usa para definir una función?",
                    "opciones": ["1) function", "2) def", "3) func"],
                    "correcta": 2
                },
                {
                    "pregunta": "¿Cuál es el resultado de la operación `3 ** 2`?",
                    "opciones": ["1) 6", "2) 9", "3) 8"],
                    "correcta": 2
                }
            ],
            "niveles": [
                (0, 20, "Junior Debugger 🐛", "¡Estás dando tus primeros pasos! Revisa bien la sintaxis."),
                (40, 60, "Desarrollador Python 🐍", "¡Dominas la sintaxis básica y las estructuras fundamentales!"),
                (80, 100, "Pythonic Master 🧙‍♂️", "¡Escribes código limpio y eficiente como un verdadero experto!")
            ]
        }
    }

    # Menú de selección
    print("=" * 45)
    print("      BIENVENIDO AL PORTAL DE QUIZZES")
    print("=" * 45)
    print("1. Cultura General de Venezuela")
    print("2. My Hero Academia")
    print("3. Programación en Python")
    
    opcion = input("\nSelecciona el número del quiz que deseas realizar (1-3): ").strip()

    if opcion not in quizzes:
        print("\n❌ Opción inválida. Inténtalo de nuevo.")
        return

    quiz_seleccionado = quizzes[opcion]
    puntos = 0
    puntos_por_pregunta = 20

    print(f"\n--- INICIANDO QUIZ: {quiz_seleccionado['titulo']} ---")
    print("Cada respuesta correcta vale 20 puntos.\n")

    # Bucle para realizar las preguntas
    for i, q in enumerate(quiz_seleccionado["preguntas"], 1):
        print(f"Pregunta {i}: {q['pregunta']}")
        for opcion_texto in q["opciones"]:
            print(f"  {opcion_texto}")
        
        while True:
            try:
                respuesta = int(input("Tu respuesta (1-3): "))
                if respuesta in [1, 2, 3]:
                    break
                print("Por favor, ingresa un número entre 1 y 3.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        if respuesta == q["correcta"]:
            print("  ¡Correcto! (+20 puntos)\n")
            puntos += puntos_por_pregunta
        else:
            print(f"  Incorrecto. La opción correcta era la {q['correcta']}.\n")

    # Determinar el nivel según la puntuación
    nivel_obtenido = ""
    descripcion_nivel = ""

    for min_p, max_p, titulo_nivel, desc in quiz_seleccionado["niveles"]:
        if min_p <= puntos <= max_p:
            nivel_obtenido = titulo_nivel
            descripcion_nivel = desc
            break

    # Resultados finales
    print("=" * 45)
    print("             RESULTADOS FINALES")
    print("=" * 45)
    print(f"Puntuación Total: {puntos} / 100 puntos")
    print(f"Nivel Alcanzado : {nivel_obtenido}")
    print(f"Comentario      : {descripcion_nivel}")
    print("=" * 45)

# Para ejecutar la función
quiz_interactivo()