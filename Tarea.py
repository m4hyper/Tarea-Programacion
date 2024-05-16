
#Tarea 1 
def division_sumas_resta(a, b):
    cociente = 0
    resto = a
    
    while resto >= b:
        resto = resto - b
        cociente = cociente + 1
    
    print("Por lo tanto, el cociente es", cociente, "(se ejecutan", cociente, "iteraciones) y el resto es", resto, "(sobran", resto, "unidades)")

# Solicitar al usuario que ingrese los números a y b
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

# Llamar a la función con los números ingresados
division_sumas_resta(a, b)


#tarea 2 

def venta_pasajes():
    destinos = {
        1: {"nombre": "Santiago", "precio": 18000},
        2: {"nombre": "Arica", "precio": 18500},
        3: {"nombre": "Temuco", "precio": 20580},
        4: {"nombre": "Concepción", "precio": 18600}
    }
    
    total_ventas = 0
    ventas_por_destino = {1: 0, 2: 0, 3: 0, 4: 0}
    total_maletas = 0
    
    while True:
        print("*************PASAJE INTERURBANOS*****************")
        print("Destinos:")
        for key, value in destinos.items():
            print(f"{key}. {value['nombre']} ${value['precio']} por tramo")
        
        destino_elegido = int(input("Seleccione un destino: "))
        ida_vuelta = input("¿Desea pasaje de vuelta? (si/no): ")
        maletas = int(input("Ingrese la cantidad de maletas: "))
        
        precio_destino = destinos[destino_elegido]["precio"]
        if ida_vuelta.lower() == "si":
            precio_destino *= 2
        
        if maletas > 1:
            total_maletas += (maletas - 1) * 5000
        
        total_venta = precio_destino + total_maletas
        total_ventas += total_venta
        ventas_por_destino[destino_elegido] += 1
        
        print("Destino:", destinos[destino_elegido]["nombre"], "ida y vuelta Valor$", precio_destino)
        print("Unidades equipaje:", maletas, "Valor $", total_maletas)
        print("TOTAL: $", total_venta)
        print("****************************************************")
        
        continuar = input("¿Necesita otro pasaje? (si/no): ")
        if continuar.lower() != "si":
            break
    
    print("*************PASAJE INTERURBANOS*****************")
    print("Resumen de Ventas del día")
    for key, value in destinos.items():
        print(value["nombre"], ventas_por_destino[key])
    print("TOTAL EN PASAJES: $", total_ventas)
    print("TOTAL EN MALETAS : $", total_maletas)
    print("****************************************************")

# Llamar a la función para iniciar la venta de pasajes
venta_pasajes()

#Pregunta 3 
def sistema_ventas_confiteria():
    categorias = {
        "dulces": {"Galletas": 1300, "Caramelos": 1000, "Chocolates": 1500},
        "salados": {"Papas Fritas": 1200, "Frutos Secos": 800, "Snacks": 1000},
        "helados": {"Helado de Chocolate": 2000, "Helado de Vainilla": 1800, "Helado de Frutilla": 1900},
        "colaciones": {"Sándwich de Jamón y Queso": 2500, "Empanadas": 1800, "Barrita de Cereal": 500}
    }
    
    descuento_por_cantidad = 0.02
    descuento_por_variedad = 0.1
    descuento_debito = 0.02
    total_compra = 0
    descuentos_aplicados = 0
    
    factura = "**************** Factura ****************\n"
    
    nombre_cliente = input("Ingrese su nombre: ")
    direccion_cliente = input("Ingrese su dirección: ")
    
    for categoria, productos in categorias.items():
        print(f"Categoría: {categoria}")
        for producto, precio in productos.items():
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
            subtotal = cantidad * precio
            total_compra += subtotal
            factura += f"\n- Producto: {producto}\nCantidad: {cantidad}\nPrecio unitario: ${precio}\nSubtotal: ${subtotal}\n"
            
            if cantidad > 5:
                descuentos_aplicados += subtotal * descuento_por_cantidad
            if cantidad >= 10:
                descuentos_aplicados += subtotal * descuento_por_variedad
    
    forma_pago = input("Ingrese la forma de pago (tarjeta de crédito, débito o transferencia bancaria): ")
    if forma_pago.lower() == "débito":
        descuentos_aplicados += total_compra * descuento_debito
    
    total_pagar = total_compra - descuentos_aplicados
    
    factura += f"\nDescuentos aplicados:\n- Descuentos por cantidad en la misma categoría: ${descuentos_aplicados}\n- Descuentos por comprar en todas las categorías: ${descuentos_aplicados}\n- Descuentos por pago con tarjeta de débito: ${descuentos_aplicados}\nTotal a pagar: ${total_pagar}\n**************************************"
    
    print(factura)

# Llamar a la función para iniciar el sistema de ventas de confitería
sistema_ventas_confiteria()

#pregunta 4 

def menu_principal():
    print("--> Bienvenido a Comida al paso <--")
    print("1. Registrar Venta")
    print("2. Consultar Ventas")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")
    return opcion

def menu_ventas():
    print("1. Hamburguesa")
    print("2. Completo")
    print("3. Papas Fritas")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

def vender_hamburguesa():
    ingredientes = {
        "Palta": 800,
        "Tomate": 700,
        "Cebolla": 600,
        "Mayonesa": 500,
        "Mostaza": 400
    }
    precio_pan = 1000
    precio_hamburguesa = 1500
    
    total_venta = precio_pan + precio_hamburguesa
    print("HAMBURGUESA")
    for ingrediente, precio in ingredientes.items():
        respuesta = input(f"Desea {ingrediente} (sí/no): ")
        if respuesta.lower() == "sí":
            total_venta += precio
    
    print("Su venta es de:", total_venta)

# Función principal para el sistema de ventas
def sistema_ventas_comida_rapida():
    ventas_totales = 0
    
    while True:
        opcion_principal = menu_principal()
        
        if opcion_principal == "1":
            opcion_venta = menu_ventas()
            
            if opcion_venta == "1":
                vender_hamburguesa()
            elif opcion_venta == "2":
                # Lógica para vender completo
                pass
            elif opcion_venta == "3":
                # Lógica para vender papas fritas
                pass
            elif opcion_venta == "4":
                continue
        elif opcion_principal == "2":
            print("El total de ventas hasta el momento es de:", ventas_totales)
        elif opcion_principal == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Llamar a la función para iniciar el sistema de ventas de comida rápida
sistema_ventas_comida_rapida()
