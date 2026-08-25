#Cuenta cuántas veces aparece una palabra en una lista de palabras.

from collections import Counter

palabras = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
frecuencias = Counter(palabras)

print(frecuencias) 