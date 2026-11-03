
# aplicar las reglas del negocio
from modelo import Producto


class ProductoServicio:

    def __init__(self, dao):
        self.dao = dao

    # 1. REGISTRAR PRODUCTO
    def registrar(self, nombre, precio, stock):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = Producto(None, nombre.strip(), precio, stock)

        return self.dao.crear(producto)

    # 2. LISTAR PRODUCTOS
    def listar(self):
        return self.dao.listar()

    # 3. BUSCAR PRODUCTO
    def buscar(self, id):

        producto = self.dao.buscar(id)

        if producto is None:
            raise ValueError("No existe un videojuego con ese ID")

        return producto

    # 4. ACTUALIZAR PRODUCTO
    def actualizar(self, id, nombre, precio, stock):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = self.buscar(id)

        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.stock = stock

        return self.dao.actualizar(producto)

    # 5. ELIMINAR PRODUCTO
    def eliminar(self, id):

        self.buscar(id)

        return self.dao.eliminar(id)

    # 6. VENDER UNIDADES
    def vender(self, id, cantidad):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        producto = self.buscar(id)

        if cantidad > producto.stock:
            raise ValueError("No hay suficientes unidades disponibles")

        nuevo_stock = producto.stock - cantidad

        self.dao.actualizar_stock(id, nuevo_stock)

        return nuevo_stock
