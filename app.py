print("gestion de ventas de usuario")
nombre_cliente = input("ingrese su nombre:")
precio_unitario = float(input("ingrese el precio unitario del producto"))
cantidad_producto = int(input("ingrese la cantidad de sus productos"))
membresia_VIP_input = input("cuenta con membresia VIP? (si/no):").strip().lower()
es_VIP = membresia_VIP_input =="si"
subtotal = precio_unitario*cantidad_producto
descuento = 0.0
if es_VIP:
    descuento= subtotal*0.10
    total_final = subtotal- descuento
    print("\n----- RESUMEN DE LA VENTA -----")
    print(f"Cliente: {nombre_cliente}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total final a pagar: ${total_final:.2f}")
    print("--------------------------------")