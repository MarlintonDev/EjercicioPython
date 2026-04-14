Compra = float(input("Ingrese el valor de la compra: "))
if Compra > 1000000:
    Descuento = Compra * 0.10
    Total_a_pagar = Compra - Descuento
    print(f"El valor de la compra es: ${Compra:,.2f}")
    print(f"El descuento aplicado es: ${Descuento:,.2f}")
    print(f"El total a pagar es: ${Total_a_pagar:,.2f}")
else:
    print(f"El valor de la compra es: ${Compra:,.0f}")
    print("No se aplica descuento para compras menores o iguales a $1,000,000")