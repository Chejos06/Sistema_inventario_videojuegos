
# mostrar el menu y recibir datos

from base_datos import inicializar_bd
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio


# Funcion para solicitar numeros enteros
def leer_entero(mensaje):

    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            print("Error: debe ingresar un numero entero.")


# Funcion para mostrar los datos de un producto
def mostrar_producto(producto):

    print("\nID:", producto.id)
    print("Nombre:", producto.nombre)
    print("Precio: $", producto.precio)
    print("Stock:", producto.stock)


# Preparar la base de datos
inicializar_bd()

# Crear el objeto DAO
dao = ProductoDAO()

# Crear el objeto servicio
servicio = ProductoServicio(dao)


# MENU PRINCIPAL
while True:

    print("\n========== INVENTARIO DE VIDEOJUEGOS ==========")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")

    opcion = leer_entero("Seleccione una opcion: ")

    # 1. REGISTRAR VIDEOJUEGO
    if opcion == 1:

        print("\n--- REGISTRAR VIDEOJUEGO ---")

        nombre = input("Nombre del videojuego: ")
        precio = leer_entero("Precio: ")
        stock = leer_entero("Cantidad disponible: ")

        try:
            producto = servicio.registrar(nombre, precio, stock)

            print("\nProducto registrado correctamente.")
            print("ID asignado:", producto.id)

        except ValueError as error:
            print("Error:", error)

    # 2. MOSTRAR INVENTARIO
    elif opcion == 2:

        print("\n--- INVENTARIO DE VIDEOJUEGOS ---")

        productos = servicio.listar()

        if productos:
            for producto in productos:
                mostrar_producto(producto)
                print("-----------------------------")
        else:
            print("No hay videojuegos registrados.")

    # 3. BUSCAR VIDEOJUEGO
    elif opcion == 3:

        print("\n--- BUSCAR VIDEOJUEGO ---")

        id = leer_entero("Ingrese el ID del videojuego: ")

        try:
            producto = servicio.buscar(id)

            print("\nVideojuego encontrado:")
            mostrar_producto(producto)

        except ValueError as error:
            print("Error:", error)

    # 4. ACTUALIZAR VIDEOJUEGO
    elif opcion == 4:

        print("\n--- ACTUALIZAR VIDEOJUEGO ---")

        id = leer_entero("Ingrese el ID del videojuego: ")

        try:
            producto = servicio.buscar(id)

            print("\nDatos actuales:")
            mostrar_producto(producto)

            nombre = input("\nNuevo nombre: ")
            precio = leer_entero("Nuevo precio: ")
            stock = leer_entero("Nuevo stock: ")

            servicio.actualizar(id, nombre, precio, stock)

            print("\nProducto actualizado correctamente.")

        except ValueError as error:
            print("Error:", error)

    # 5. ELIMINAR VIDEOJUEGO
    elif opcion == 5:

        print("\n--- ELIMINAR VIDEOJUEGO ---")

        id = leer_entero("Ingrese el ID del videojuego: ")

        try:
            producto = servicio.buscar(id)

            print("\nVideojuego que se eliminara:")
            mostrar_producto(producto)

            confirmacion = input("\n¿Desea eliminarlo? (s/n): ")

            if confirmacion.lower() == "s":
                servicio.eliminar(id)
                print("Producto eliminado correctamente.")
            else:
                print("Operacion cancelada.")

        except ValueError as error:
            print("Error:", error)

    # 6. VENDER UNIDADES
    elif opcion == 6:

        print("\n--- VENDER VIDEOJUEGO ---")

        id = leer_entero("Ingrese el ID del videojuego: ")
        cantidad = leer_entero("Cantidad de unidades a vender: ")

        try:
            nuevo_stock = servicio.vender(id, cantidad)

            print("\nVenta realizada correctamente.")
            print("Unidades restantes:", nuevo_stock)

        except ValueError as error:
            print("Error:", error)

    # 7. SALIR
    elif opcion == 7:

        print("\nGracias por utilizar el sistema.")
        print("Aplicacion finalizada.")
        break

    else:
        print("Opcion no valida. Intente nuevamente.")
