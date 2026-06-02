def practicar():
    lista_nombres:list[str] = ['VerOnica','roberto','JOSE','   Kimberly','Mauricio Andres   ','Cris']
    lista_nombres_limpios:list[str] = []

    for nombre in lista_nombres:
        nombre_limpio = nombre.strip().capitalize()
        lista_nombres_limpios.append(nombre_limpio)
    
    lista_nueva:list[str] = [  x.strip().capitalize()  for  x in lista_nombres   ]

    lista_largos:list[int] = [ len(x) for x in lista_nueva ]

    lista_nombre_largos = list(zip(lista_nueva,lista_largos))
    print(lista_nombre_largos)

if __name__ == "__main__":
    practicar()