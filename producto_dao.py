
# ejecutar las operaciones sql
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:

    # 1. CREAR UN PRODUCTO
    def crear(self, producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO productos (nombre, precio, stock)
            VALUES (?, ?, ?)
        """

        cursor.execute(sql, (producto.nombre, producto.precio, producto.stock))
        producto.id = cursor.lastrowid

        conexion.commit()
        conexion.close()

        return producto

    # 2. LISTAR TODOS LOS PRODUCTOS
    def listar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()

        productos = []

        for fila in resultados:
            producto = Producto(fila[0], fila[1], fila[2], fila[3])
            productos.append(producto)

        conexion.close()

        return productos

    # 3. BUSCAR UN PRODUCTO POR ID
    def buscar(self, id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        fila = cursor.fetchone()

        conexion.close()

        if fila:
            producto = Producto(fila[0], fila[1], fila[2], fila[3])
            return producto

        return None

    # 4. ACTUALIZAR UN PRODUCTO
    def actualizar(self, producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?
            WHERE id = ?
        """

        cursor.execute(sql, (
            producto.nombre,
            producto.precio,
            producto.stock,
            producto.id
        ))

        conexion.commit()

        resultado = cursor.rowcount

        conexion.close()

        return resultado > 0

    # 5. ELIMINAR UN PRODUCTO
    def eliminar(self, id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))

        conexion.commit()

        resultado = cursor.rowcount

        conexion.close()

        return resultado > 0

    # 6. ACTUALIZAR EL STOCK DESPUES DE UNA VENTA
    def actualizar_stock(self, id, nuevo_stock):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "UPDATE productos SET stock = ? WHERE id = ?",
            (nuevo_stock, id)
        )

        conexion.commit()

        resultado = cursor.rowcount

        conexion.close()

        return resultado > 0
