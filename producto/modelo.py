from typing import TypedDict

class Producto(TypedDict):  
    codigo: str
    nombre: str
    precio: float
    cantidad: int
    activo: bool

_productos:dict[str, Producto] = {}

def verificar_codigo_producto(codigo:str) -> bool:
    return codigo in _productos

def agregar_producto(codigo:str, nombre:str, precio:float, cantidad:int, activo:bool) -> bool, str:
    codigo = codigo.strip().upper()
    if verificar_codigo_producto(codigo):
        return False, 'El codigo ya existe'
    else:
        producto:Producto = {
            'codigo': codigo,
            'nombre': nombre.strip(),
            'precio': precio,
            'cantidad': cantidad,
            'activo': activo
        }
        _productos[producto['codigo']] = producto
        return True, 'Producto agregado exitosamente'

