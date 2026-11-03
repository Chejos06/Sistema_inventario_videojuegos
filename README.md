Sistema de Inventario de Videojuegos

1. Descripción del proyecto

El Sistema de Inventario de Videojuegos es una aplicación desarrollada en Python que permite administrar los videojuegos de una tienda mediante un menú interactivo de consola. 
El programa utiliza SQLite para almacenar la información, permitiendo registrar, consultar, actualizar y eliminar productos, además de controlar las unidades disponibles mediante operaciones de venta.

2. Objetivo
Desarrollar una aplicación que permita gestionar un inventario de videojuegos utilizando operaciones CRUD, archivos de base de datos SQLite y el patrón DAO para separar las responsabilidades del programa.

3. Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

- main.py: contiene el menú principal y permite al usuario interactuar con el sistema.
- modelo.py: contiene la clase Producto, encargada de representar los videojuegos.
- base_datos.py: administra la conexión con SQLite y la creación de la tabla de productos.
- producto_dao.py: contiene las operaciones SQL para registrar, listar, buscar, actualizar y eliminar productos, además de actualizar el stock.
- producto_servicio.py: contiene las validaciones y reglas del negocio para las operaciones del inventario.

4. Funcionalidades implementadas

El sistema cuenta con las siguientes opciones:

1. Registrar videojuegos.
2. Mostrar todos los videojuegos registrados.
3. Buscar videojuegos mediante su ID.
4. Actualizar nombre, precio y stock.
5. Eliminar videojuegos.
6. Vender unidades y descontarlas del inventario.
7. Salir del programa.

5. Validaciones

El programa controla las siguientes situaciones:

- No permite registrar nombres vacíos.
- No permite precios menores o iguales a cero.
- No permite cantidades de inventario negativas.
- No permite realizar ventas con cantidades menores o iguales a cero.
- No permite vender más unidades de las disponibles.
- Informa cuando un videojuego no existe.
- Controla las entradas incorrectas para evitar que el programa se cierre inesperadamente.

6. Base de datos

La aplicación utiliza SQLite para almacenar la información de los videojuegos.
La tabla productos contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| id | Identificador único del producto |
| nombre | Nombre del videojuego |
| precio | Precio del videojuego |
| stock | Cantidad disponible |

La información permanece guardada entre las ejecuciones del programa.

7. Instrucciones para ejecutar el programa

Requisitos:
- Tener Python instalado.
- Contar con los archivos del proyecto en una misma carpeta.

Pasos:

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Abrir una terminal en esa ubicación.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

La base de datos `tienda.db` se creará automáticamente al iniciar la aplicación si todavía no existe.

Conclusión
El desarrollo de este proyecto permitió aplicar los conocimientos de Python, programación orientada a objetos, bases de datos SQLite y separación de responsabilidades mediante el patrón DAO.
Se logró implementar un sistema funcional para administrar un inventario de videojuegos, incluyendo operaciones CRUD, ventas y validaciones para mantener un control adecuado de los productos.
