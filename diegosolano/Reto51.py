def inator_nombre(nombre_usuario):
    # .strip() elimina espacios innecesarios al inicio o al final
    nombre_limpio = nombre_usuario.strip()
    return f"{nombre_limpio}-inator"

# Ejemplo de uso interactivo:
usuario = input("Ingresa tu nombre de usuario: ")
resultado = inator_nombre(usuario)

print(f"Tu nuevo nombre de villano es: {resultado}")