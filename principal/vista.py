from eii_utils import mostrar_menu

def crear_vista_menu_principal() -> int:
    return mostrar_menu('Menu Principal', ['Administrar productos', 'Administrar clientes'])

def crear_vista_finalizacion() -> None:
    print('Gracias por usar el programa')                    