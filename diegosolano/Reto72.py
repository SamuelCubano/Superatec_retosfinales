# --- SUBMENÚ GENÉRICO Y DINÁMICO ---

def realizar_conversion(titulo, opciones, tabla_factores):
    print(f"\n--- CONVERSIÓN DE {titulo.upper()} ---")
    
    # Mostrar lista de unidades disponibles
    for clave, nombre in opciones.items():
        print(f"{clave}. {nombre}")
        
    orig = input("\nElige la unidad DE ORIGEN: ").strip()
    dest = input("Elige la unidad DE DESTINO: ").strip()

    if orig not in opciones or dest not in opciones:
        print("❌ Opción inválida. Asegúrate de elegir números de la lista.")
        return

    try:
        val = float(input(f"Ingresa la cantidad en {opciones[orig]}: "))
        if titulo != "Temperatura" and val < 0:
            print("❌ La cantidad no puede ser negativa.")
            return
            
        resultado = tabla_factores(orig, dest, val)
        print(f"\n👉 Resultado: {val} {opciones[orig]} = {resultado:.2f} {opciones[dest]}")
    except ValueError:
        print("❌ Ingresa un número válido.")


# --- LÓGICA DE CÁLCULO ---

def calcular_monedas(de, a, val):
    # Tasas base en referencia al Dólar (USD)
    tasas = {
        "1": 40.0,   # Bolívares (VES)
        "2": 1.0,    # Dólar (USD)
        "3": 0.92    # Euro (EUR)
    }
    # Convierte a USD y luego a la moneda destino
    monto_en_usd = val / tasas[de]
    return monto_en_usd * tasas[a]


def calcular_temperatura(de, a, val):
    # Primero convertimos todo a Celsius
    if de == "1": c = val
    elif de == "2": c = (val - 32) * 5 / 9
    elif de == "3": c = val - 273.15

    # De Celsius convertimos a la unidad de destino
    if a == "1": return c
    elif a == "2": return (c * 9 / 5) + 32
    elif a == "3": return c + 273.15


def calcular_unidades(de, a, val):
    # Factores de conversión a la unidad base del grupo
    # Grupo 1-2: Masa (base kg), 3-4: Longitud (base m), 5-6: Capacidad (base L)
    base_masa = {"1": 1.0, "2": 0.453592}       # Kg, Lbs
    base_long = {"3": 1.0, "4": 0.3048}         # Metros, Pies
    base_cap  = {"5": 1.0, "6": 3.78541}        # Litros, Galones

    # Validar que no se mezclen tipos incompatibles (ej. Masa con Longitud)
    if (de in base_masa and a in base_masa):
        return (val * base_masa[de]) / base_masa[a]
    elif (de in base_long and a in base_long):
        return (val * base_long[de]) / base_long[a]
    elif (de in base_cap and a in base_cap):
        return (val * base_cap[de]) / base_cap[a]
    else:
        print("\n⚠️ No se pueden convertir unidades de diferente tipo (ej. Masa a Longitud).")
        return val


# --- MENÚ PRINCIPAL ---

def menu_convertidor():
    monedas = {"1": "Bolívares (VES)", "2": "Dólares (USD)", "3": "Euros (EUR)"}
    temperaturas = {"1": "Celsius (°C)", "2": "Fahrenheit (°F)", "3": "Kelvin (K)"}
    unidades = {
        "1": "Kilogramos (kg)", "2": "Libras (lb)",
        "3": "Metros (m)", "4": "Pies (ft)",
        "5": "Litros (L)", "6": "Galones (gal)"
    }

    while True:
        print("\n==================================")
        print("     CONVERTIDOR MULTIUSO")
        print("==================================")
        print("1. Convertir Monedas")
        print("2. Convertir Temperatura")
        print("3. Convertir Unidades (Masa, Longitud, Capacidad)")
        print("4. Salir")
        
        opción = input("\nElige una opción (1-4): ").strip()
        
        if opción == "1":
            realizar_conversion("Monedas", monedas, calcular_monedas)
        elif opción == "2":
            realizar_conversion("Temperatura", temperaturas, calcular_temperatura)
        elif opción == "3":
            realizar_conversion("Unidades", unidades, calcular_unidades)
        elif opción == "4":
            print("\n¡Gracias por usar el convertidor! Hasta luego. 👋")
            break
        else:
            print("\n❌ Opción no válida. Por favor elige entre 1 y 4.")

# Ejecutar el programa
menu_convertidor()