# Ejercicio 29: Pide una contraseña; mientras sea incorrecta sigue pidiéndola (la correcta es "python123").

def verificar_contraseña():
    CLAVE_CORRECTA = "python123"
    password = ""

    while password != CLAVE_CORRECTA:
        password = input("Ingrese la contraseña: ")
        if password != CLAVE_CORRECTA:
            print("Contraseña incorrecta. Intente de nuevo.\n")

    print("\n--- ACCESO CONCEDIDO ---")
    print("Bienvenido al sistema.")

verificar_contraseña()