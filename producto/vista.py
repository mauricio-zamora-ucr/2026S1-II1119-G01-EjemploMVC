from eii_utils import mostrar_menu, pausar, leer_entero, leer_flotante, leer_booleano, leer_texto

def crear_vista_menu_productos() -> int:
    return mostrar_menu('Menu Productos', 
    ['Agregar producto', 'Modificar producto', 'Eliminar producto', 'Listar productos','Reporte productos'],
    'Volver al menu principal')

def crear_vista_agregar_producto() -> tuple[str, str, float, int, bool]:
    codigo = leer_texto('Ingrese el codigo del producto: ')
    nombre = leer_texto('Ingrese el nombre del producto: ')
    precio = leer_flotante('Ingrese el precio del producto: ')
    cantidad = leer_entero('Ingrese la cantidad del producto: ')
    activo = leer_booleano('¿El producto esta activo?')
    return codigo, nombre, precio, cantidad, activo