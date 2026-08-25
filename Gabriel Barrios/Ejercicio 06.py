# 	Ejercicio 06: Convierte una cantidad de minutos en horas y minutos (ej: 130 min → 2 h 10 min).

def convertir_minutos(minutos: int) -> str:
    """Convierte minutos al formato visual 'X h Y min'."""
    horas, mins = divmod(minutos, 60)
    return f"{horas} h {mins} min"

# Grupo de datos a procesar
tiempos_minutos = [130, 45, 300, 75, 0, 500]

# Procesamiento funcional en lote (usando map)
resultados = list(map(convertir_minutos, tiempos_minutos))

# Impresión formateada del grupo
print("--- RESULTADOS EN LOTE ---")
for entrada, salida in zip(tiempos_minutos, resultados):
    print(f"  {entrada:>4} min  ➔  {salida}")