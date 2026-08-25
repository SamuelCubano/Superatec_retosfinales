# Ejercicio 08: Pide el precio unitario de una camiseta y calcula el total por la compra de 3, con 10% de descuento.

def calcular_compra_camisetas():
    try:
        precio_unitario = float(input("Ingrese el precio unitario de la camiseta ($): "))
        
        CANTIDAD = 3
        DESCUENTO_PORCENTAJE = 0.10  # 10%
        
        subtotal = precio_unitario * CANTIDAD
        monto_descuento = subtotal * DESCUENTO_PORCENTAJE
        total = subtotal - monto_descuento
        
        print("\n--- RESUMEN DE LA COMPRA ---")
        print(f" Cantidad:          {CANTIDAD} camisetas")
        print(f" Precio unitario:   ${precio_unitario:,.2f}")
        print(f" Subtotal:          ${subtotal:,.2f}")
        print(f"  Descuento (10%):  -${monto_descuento:,.2f}")
        print(f" Total a pagar:     ${total:,.2f}")

    except ValueError:
        print(" Error: Por favor, ingrese un monto numérico válido.")

calcular_compra_camisetas()