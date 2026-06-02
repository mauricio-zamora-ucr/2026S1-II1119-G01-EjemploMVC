from eii_utils import mostrar_menu, pausar

def crear_vista_menu_productos() -> int:
    return mostrar_menu('Menu Productos', 
    ['Agregar producto', 'Modificar producto', 'Eliminar producto', 'Listar productos','Reporte productos'],
    'Volver al menu principal')

