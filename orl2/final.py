def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejemplo de uso
c = float(input("Introduce la temperatura en grados Celsius: "))
f = celsius_a_fahrenheit(c)

print(f"{c}°C equivalen a {f}°F")