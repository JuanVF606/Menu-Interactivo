import Buscaminas, TresEnRayas

def CategoriaJuegos(opcion):
    if opcion == 1:
        Buscaminas.Menu()
    if opcion ==2:
        TresEnRayas.JUEGO()

import os
def Menu():
    print('Bienvenido Al Menu interactivo')
    print('------------------------------')
    Categorias =int(input(' 1.Buscaminas 2.Tres en raya: '))
    os.system("cls")
    CategoriaJuegos(Categorias)


#BLOQUE PRINCIPAL

Menu()