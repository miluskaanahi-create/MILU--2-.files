# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.
    
    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar. Por defecto es 10%.
    
    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
def main():
    print("=== Calculadora de Descuentos ===\n")
    
    # Entrada del usuario para la primera compra (descuento por defecto)
    monto_compra1 = float(input("Ingrese el monto total de la primera compra: $"))
    descuento1 = calcular_descuento(monto_compra1)  # usa el descuento por defecto
    total_pagar1 = monto_compra1 - descuento1
    print("\n--- Resultado Compra 1 ---")
    print(f"Monto total: ${monto_compra1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${total_pagar1:.2f}\n")
    
    # Entrada del usuario para la segunda compra (descuento personalizado)
    monto_compra2 = float(input("Ingrese el monto total de la segunda compra: $"))
    porcentaje_descuento2 = float(input("Ingrese el porcentaje de descuento a aplicar: "))
    descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
    total_pagar2 = monto_compra2 - descuento2
    print("\n--- Resultado Compra 2 ---")
    print(f"Monto total: ${monto_compra2:.2f}")
    print(f"Descuento aplicado ({porcentaje_descuento2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${total_pagar2:.2f}")

# Llamada al programa principal
if __name__ == "__main__":
    main()
