import Buscaminas 


def CategoriaJuegos(opcion):
    if opcion == 1:
        Buscaminas.Menu()


def Menu():
    print('Bienvenido Al Menu interactivo')
    print('------------------------------')
    Categorias =int(input(' 1.Buscaminas 2.Tres en raya'))
    CategoriaJuegos(Categorias)

#BLOQUE PRINCIPAL
  
Menu() 