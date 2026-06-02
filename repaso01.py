def practicar():
    lista_nombres:list[str] = ['VerOnica','roberto','JOSE','   Kimberly','Mauricio Andres   ','Cris']
    lista_nombres_limpios:list[str] = []

    for nombre in lista_nombres:
        nombre_limpio = nombre.strip().capitalize()
        lista_nombres_limpios.append(nombre_limpio)
    
    lista_nueva:list[str] = [  x.strip().capitalize()  for  x in lista_nombres   ]

    lista_largos:list[int] = [ len(x) for x in lista_nueva ]
    print('lista largos', lista_largos)

    print('lista nueva', lista_nueva)

    print(lista_nombres_limpios)

if __name__ == "__main__":
    practicar()