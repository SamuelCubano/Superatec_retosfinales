from collections import deque

# Crear la fila del banco con personas en orden de llegada
fila_banco = deque(["Carlos", "María", "José", "Ana", "Luis"])

print("--- Inicio de atención en el banco ---")

# Atender a las personas una por una hasta que la fila esté vacía
while fila_banco:
    persona_atendida = fila_banco.popleft()
    print(f"Atendiendo a: {persona_atendida}")
    print(f"Personas restantes en la fila: {len(fila_banco)}")
    print("-" * 35)

print("¡La fila está vacía! Se han atendido a todas las personas.")