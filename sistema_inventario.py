inventario = {
    "Producto1": {"Nombre":"Teclado","Costo":45000,"Stock":15},
    "Producto2":{"Nombre":"Mouse","Costo":30000,"Stock":20},
    "Producto3":{"Nombre":"Monitor","Costo":95000,"Stock":10},
    "Producto4":{"Nombre":"Auriculares","Costo":50000,"Stock":30}
}
def mostrar_producto():
    print("\n" + "=" * 43)
    for producto, datos in inventario.items():
        print(f"Código: {producto}  | {datos['Nombre']}")
        print(f"   Precio: ${datos['Costo']}  | Stock: {datos['Stock']}")
        print("-" * 43)
    print()
def actualizar_stock(producto, cantidad):
    inventario[producto]["Stock"] += cantidad
def calcular_valor_total():
    valor_total = 0
    for i in inventario:
        valor_total+= inventario[i]["Stock"] * inventario[i]["Costo"]
    print(f"Valor total: {valor_total:.2f}")

while True:
    try:
        opcion= int(input("""-----------Sistema de Inventario-----------
        1. Mostrar productos
        2. Actualizar stock
        3. Calcular valor total de todos los productos
        4. Salir del menú
           Ingrese una opcion: """))
    except ValueError:
        print("Error, Ingrese una opción válida")
    if opcion == 1:
        mostrar_producto()
    elif opcion == 2:
        while True:
            producto =""
            while True:
                if producto != "":
                    break
                producto = input("Ingrese código del producto: ")
                if producto in inventario:
                        break;
                else:
                    producto = ""
                    print("Producto no encontrado")
            while True:
                try:
                    cantidad = int(input("Ingrese stock nuevo: "))
                    actualizar_stock(producto,cantidad)
                    print("Stock actualizado")
                    break
                except ValueError:
                    print("Error, ingrese una cantidad válida")
            break
    elif opcion == 3:
        calcular_valor_total()
    elif opcion == 4:
        break
print("Saliendo del sistema de inventario")