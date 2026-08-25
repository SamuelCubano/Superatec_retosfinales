def potencia(base, exponente):
    # Caso especial: cualquier número elevado a 0 es 1 (excepto 0^0, pero por convención da 1)
    if exponente == 0:
        return 1
    
    # Manejamos exponentes negativos
    es_negativo = exponente < 0
    exponente_absoluto = abs(exponente)
    
    resultado = 1
    # Bucle para multiplicar la base tantas veces como indique el exponente absoluto
    for _ in range(exponente_absoluto):
        resultado *= base
        
    # Si el exponente era negativo, devolvemos el inverso multiplicativo (1 / resultado)
    if es_negativo:
        return 1 / resultado
    
    return resultado


# Ejemplos de uso:
print(potencia(2, 3))   # Salida: 8
print(potencia(2, -2))  # Salida: 0.25 (1 / (2^2))
print(potencia(5, 0))   # Salida: 1