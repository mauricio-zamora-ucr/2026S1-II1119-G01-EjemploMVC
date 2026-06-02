import producto.modelo as modelo
import producto.vista as vista
from eii_utils import imprimir_mensaje, imprimir_error, pausar

def agregar_producto(codigo, nombre, precio, cantidad, activo) -> tuple[bool, str]:
    if precio < 0:
        return False, 'El precio no puede ser negativo'
    if cantidad < 0:
        return False, 'La cantidad no puede ser negativa'
    codigo = codigo.strip().upper()
    if modelo.verificar_codigo_producto(codigo):
        return False, 'El codigo ya existe'
    nombre = nombre.strip().upper()
    return modelo.agregar_producto(codigo, nombre, precio, cantidad, activo)

def iniciar_menu_productos() -> None:
    opcion:int = -1
    while opcion != 0:
        opcion = vista.crear_vista_menu_productos()
        match opcion:
            case 1:
                codigo, nombre, precio, cantidad, activo = vista.crear_vista_agregar_producto()
                salida, mensaje = agregar_producto(codigo, nombre, precio, cantidad, activo)
                if salida:
                    imprimir_mensaje(mensaje)
                else:
                    imprimir_error(mensaje)
                pausar()
            case 2:
                print('Muy pronto la modificacion de productos')
            case 3:
                print('Muy pronto la eliminacion de productos')
            case 4:
                print('Muy pronto la lista de productos')
            case 5:
                print('Muy pronto el reporte de productos')