from eii_utils import limpiar_consola, pausar
#from principal.vista import crear_vista_menu_principal, crear_vista_finalizacion
import principal.vista as vista
from producto.controlador import iniciar_menu_productos

def iniciar_aplicacion() -> None:
    
    opcion:int = -1
    while opcion != 0:
        limpiar_consola()
        opcion = vista.crear_vista_menu_principal()
        match opcion:
            case 1:
                iniciar_menu_productos()
                pausar()
            case 2:
                print('Muy pronto los clientes')
                pausar()
            case 0:
                vista.crear_vista_finalizacion()
