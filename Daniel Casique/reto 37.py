#Invierte una lista sin usar .reverse() ni slicing ([::-1]).

def invertir_lista(lista):
    lista_invertida = []
    # Recorremos desde el último índice hasta el 0 con paso -1
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

mi_lista = [1, 2, 3, 4, 5]
print(invertir_lista(mi_lista))  # Salida: [5, 4, 3, 2, 1]