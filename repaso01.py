def segundo_elemento(x):
    return x[1]

def filtro(x):
    return x[1] == 8

def practicar():
    lista_nombres:list[str] = ['VerOnica','roberto','JOSE','   Kimberly','Mauricio Andres   ','Cris']
    lista_nombres_limpios:list[str] = []

    for nombre in lista_nombres:
        nombre_limpio = nombre.strip().capitalize()
        lista_nombres_limpios.append(nombre_limpio)
    
    lista_nueva:list[str] = [  x.strip().capitalize()  for  x in lista_nombres   ]

    lista_largos:list[int] = [ len(x) for x in lista_nueva ]

    lista_nombre_largos = list(zip(lista_nueva,lista_largos))
    lista_nombre_largos.sort(key=segundo_elemento)
    print(lista_nombre_largos)

    lista_nombre_largos.sort(key=lambda x: x[1])
    print(lista_nombre_largos)

    lista_filtrada = list(filter(filtro, lista_nombre_largos))
    print(lista_filtrada)

if __name__ == "__main__":
    practicar()