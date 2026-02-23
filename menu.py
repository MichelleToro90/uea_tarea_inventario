from app.inventario import Inventario
from app.producto import Producto

def menu():
    print("\n📦 SISTEMA DE INVENTARIOS")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Ver inventario")
    print("5. Salir")
    return input("Elige una opción: ")

def ejecutar_menu():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(codigo, nombre, cantidad, precio))

        elif opcion == "2":
            codigo = input("Código del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(codigo, cantidad, precio)

        elif opcion == "3":
            codigo = input("Código a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida")