from typing import TypedDict

class Estudiante(TypedDict):
    carne:str
    nombre: str
    edad: int

lista_estudiantes:list[Estudiante] = []

est1:Estudiante = {}
est1['carne'] = '001'
est1['nombre'] = 'Veronica'
est1['edad'] = 30

d1:dict[str, int] ={}
d1['nombre'] = 'Veronica'
d1['edad'] = 30
d2:dict[str, int] ={}
d2['nombre'] = 'Roberto'
d2['edad'] = 25
d3:dict[str, int] ={}
d3['nombre'] = 'Jose'
d3['edad'] = 35

lista_personas:list[dict[str, int]] = [d1,d2,d3]

for persona in lista_personas:
    print(persona['nombre'], persona['edad'])