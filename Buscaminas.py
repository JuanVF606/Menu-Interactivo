#Mensajes:
M1 = 'Bienvenido al Juego buscaminas'


#                           DEFINICIONES
#Configuracion del buscaminas PREDETERMINADO:
def BuscaminasPredet():
    n = 6
    T = []
    i = 1
    while (i<=n):
        F = ['.'] * n
        T.append(F)
        i = i+1
    strPos = input('Ingresa  3 posiciones aleatorias: ')
    strPos = strPos.upper()
    numMinas = 0
    i=0
    while i<len(strPos):
        if T[ord(strPos[i])-65][int(strPos[i+1])-1] != '*':
            T[ord(strPos[i])-65][int(strPos[i+1])-1] = '*'
            numMinas += 1
        i=i+2
    celdasSinMinas = n*n-numMinas
    print('', end='  ')
    j=0
    while j<n:
        print(j+1, end=' ')
        j=j+1
    print('', end='\n')
    i=0
    while i<n:
        j=0
        print(chr(i+65), end=' ') #Letra al principio de cada fila.
        while j<n:
            if T[i][j] == '*':
                print('.', end=' ')
            else:
                print(T[i][j], end=' ')
            j=j+1
        print('', end='\n')
        i=i+1
    #INICIO DEL JUEGO:
    ganaste = False
    perdiste = False
    while perdiste == False and ganaste == False:
        strPos = input('Ingresa la casilla del tablero que quieres abrir: ')
        strPos = strPos.upper()
        x = ord(strPos[0])-65
        y = int(strPos[1])-1
        if 0 <= x < n and 0 <= y < n:
            contMinas = 0
            if T[x][y] == '*':
                perdiste = True
            elif T[x][y] == '.':
                if x>0 and y>0 and T[x-1][y-1] == '*': #ARRIBA-IZQUIERDA
                    contMinas += 1
                if x>0 and T[x-1][y] == '*': #ARRIBA
                    contMinas += 1
                if x>0 and y<n-1 and T[x-1][y+1] == '*': #ARRIBA-DERECHA
                    contMinas += 1
                if y>0 and T[x][y-1] == '*': #IZQUIERDA
                    contMinas += 1
                if y<n-1 and T[x][y+1] == '*': #DERECHA
                    contMinas += 1
                if x<n-1 and y>0 and T[x+1][y-1] == '*': #ABAJO-IZQUIERDA
                    contMinas += 1
                if x<n-1 and T[x+1][y] == '*': #ABAJO
                    contMinas += 1
                if x<n-1 and y<n-1 and T[x+1][y+1] == '*': #ABAJO-DERECHA
                    contMinas += 1
                T[x][y] = str(contMinas)
                celdasSinMinas -= 1        
        if celdasSinMinas == 0:
            ganaste = True
        print('', end='  ')
        j=0
        while j<n:
            print(j+1, end=' ')
            j=j+1
        print('', end='\n')
        i=0
        while i<n:
            j=0
            print(chr(i+65), end=' ')   #Letra al principio de cada fila.
            while j<n:
                if perdiste == True or ganaste == True:
                    print(T[i][j], end=' ')
                else:
                    if T[i][j] == '*':
                        print('.', end=' ')
                    else:
                        print(T[i][j], end=' ')
                j=j+1
            print('', end='\n')
            i=i+1
        if ganaste == True:
            print('GANASTE')
        if perdiste == True:
            print('PERDISTE')        

#Configuracion Juego Buscaminas con manejo de archivos :
from random import randint
def MINAS_ALEATORIAS(Nivel_DIFICULTAD,dimension):

    if Nivel_DIFICULTAD == "F":
        Porcentaje_Minas = 10
    elif Nivel_DIFICULTAD == "M":
        Porcentaje_Minas = 15
    elif Nivel_DIFICULTAD == "D":
        Porcentaje_Minas = 20
    elif Nivel_DIFICULTAD == "X":
        Porcentaje_Minas = 30
    TOTAL = int(dimension*dimension*Porcentaje_Minas/100) #Se calcula el número concreto de minas que se deben generar usando el porcentaje, cuidando que sea un valor entero:
    Explosion = []
    i = 1
    while i <= TOTAL:
        fila = randint(1, dimension)
        columna = randint(1, dimension)
        letra = chr(fila+64)
        posMina = letra+str(columna)
        if posMina not in Explosion:
            Explosion.append(posMina)
            i = i+1
    return Explosion
 
def IMPRIME_TABLERO(T, n):
    print('  ', end='  ')
    j = 0
    for i in range(n):
        if i<9:
            print(j+1, end='  ')
            j = j+1
        else:
            print(j+1, end=' ')
            j += 1
    print('', end='\n')
    i = 0
    while i < n:
        j = 0
        print(chr(i+65), end='   ')  # Letra al principio de cada fila.
        while j < n:
            if T[i][j] == '*':
                print('.', end='  ')
            else:
                print(T[i][j], end='  ')
            j = j+1
        print('', end='\n')
        i = i+1

def TABLERO(n):
    T = []
    i = 1
    while i <= n:
        F = ['.'] * n
        T.append(F)
        i = i+1
    return T

def AJUSTES_JUEGO(fichero):
    _file = open(fichero, "r")
    Nivel_Dimension = int(_file.readline())
    Nivel_DIFICULTAD = _file.readline()
    _file.close()
    Nivel_DIFICULTAD = Nivel_DIFICULTAD.replace('\n','')
    return Nivel_Dimension, Nivel_DIFICULTAD
 
def Guarda_Minas(MINE_position, Nivel_Dimension, nombre_Documento):   
    nombre_Documento = nombre_Documento.replace("txt", "sal")
    N_document = open(nombre_Documento, "w")
    N_document.write(str(Nivel_Dimension))
    N_document.write("\n")
    for Position in MINE_position:
        N_document.write(Position)
        N_document.write("\n")
    N_document.close()

def generarTablero(fichero):
    if fichero == 'Facil.sal' or fichero =='facil.sal':
        file = open(fichero, "r")
    if fichero == 'Medio.sal'or fichero =='medio.sal':
        file = open(fichero, "r")
    if fichero == 'Dificil.sal'or fichero =='experto.sal':
        file = open(fichero, "r")
    if fichero == 'Experto.sal'or fichero =='experto.sal':
        file = open(fichero, "r")
    dimension = int(file.readline()) 
    MT = TABLERO(dimension) 
    TOTALMINAS = 0 
    for linea in file: 
        linea = linea.replace('\n','') 
        letra = linea[0] 
        numero = linea[1:] 
        fila = ord(letra)-65
        columna = int(numero)-1 
        MT[fila][columna] = "*" 
        TOTALMINAS = TOTALMINAS + 1 
    return MT, dimension, TOTALMINAS

def juego(MT,dimension,TOTALMINAS):
    IMPRIME_TABLERO(MT, dimension)
    Victoria = False
    Derrota = False
    while Derrota == False and Victoria == False:
        MINAS = input('Ingresa la casilla del tablero que quieres abrir: ') 
        MINAS = MINAS.upper() 
        if len(MINAS) == 2: 
            x = ord(MINAS[0])-65
            y = int(MINAS[1])-1
        elif len(MINAS)==3: 
            x = ord(MINAS[0])-65
            y = int(MINAS[1:])-1
        if 0 <= x < dimension and 0 <= y < dimension:
            contMinas = 0
            if MT[x][y] == '*':
                Derrota = True
            elif MT[x][y] == '.':
                if x > 0 and y > 0 and MT[x-1][y-1] == '*':  # ARRIBA-IZQUIERDA
                    contMinas += 1
                if x > 0 and MT[x-1][y] == '*':  # ARRIBA
                    contMinas += 1
                if x > 0 and y < dimension-1 and MT[x-1][y+1] == '*':  # ARRIBA-DERECHA
                    contMinas += 1
                if y > 0 and MT[x][y-1] == '*':  # IZQUIERDA
                    contMinas += 1
                if y < dimension-1 and MT[x][y+1] == '*':  # DERECHA
                    contMinas += 1
                if x < dimension-1 and y > 0 and MT[x+1][y-1] == '*':  # ABAJO-IZQUIERDA
                    contMinas += 1
                if x < dimension-1 and MT[x+1][y] == '*':  # ABAJO
                    contMinas += 1
                if x < dimension-1 and y < dimension-1 and MT[x+1][y+1] == '*':  # ABAJO-DERECHA
                    contMinas += 1
                MT[x][y] = str(contMinas)
                TOTALMINAS -= 1
        if TOTALMINAS == 0:
            Victoria = True
        #IMPRIME
        print('  ', end='  ')
        j = 0
        for i in range(dimension):
            if i<9:
                print(j+1, end='  ')
                j = j+1
            else:
                print(j+1, end=' ')
                j += 1
        print('', end='\n')
        i = 0
        while i < dimension:
            j = 0
            print(chr(i+65), end='   ')  # Letra al principio de cada fila.
            while j < dimension:
                if Derrota == True or Victoria == True:
                    print(MT[i][j], end='  ')
                else:
                    if MT[i][j] == '*':
                        print('.', end='  ')
                    else:
                        print(MT[i][j], end='  ')
                j = j+1
            print('', end='\n')
            i = i+1
        if Victoria == True:
            print('GANASTE')
        if Derrota == True:
            print('PERDISTE')
########################################################################    
def Dificultades():
    print("")
    print ("que dificultad desea?")
    print (" 1. facil.")
    print (" 2. medio.")
    print (" 3. dificil.")
    print (" 4. Experto ")
    OP = int(input("elija una opcion: "))
    if OP == 1:
        Fichero = str(input("Ingresa nombre del archivo >> Facil.sal: "))
        MT,dimension,TOTALMINAS = generarTablero(Fichero)
        juego(MT,dimension,TOTALMINAS)
    if OP == 2:
        Fichero = str(input("Ingresa nombre del archivo >> Medio.sal: "))
        MT,dimension,TOTALMINAS = generarTablero(Fichero)
        juego(MT,dimension,TOTALMINAS)
    if OP == 3:  
        Fichero = str(input("Ingresa nombre del archivo >> Dificil.sal: "))
        MT,dimension,TOTALMINAS = generarTablero(Fichero)
        juego(MT,dimension,TOTALMINAS)
    if OP == 4:
        Fichero = str(input("Ingresa nombre del archivo >> Experto.sal: "))
        MT,dimension,TOTALMINAS = generarTablero(Fichero)
        juego(MT,dimension,TOTALMINAS)

#Opciones:
def opciones():
    _print = int(input('(1) Tablero Personalizado. (2) Tablero con manejos de Archivos. (3) Tablero con ingreso de minas por el Usuario. (4) Salir:  '))
    if _print == 1:
        print('Proximamente')
    if _print == 2:
        Dificultades()
    if _print == 3:
        BuscaminasPredet()
        
#Menu Del juego:
def Menu():
    print("\t",'◙'*len(M1))    
    print("\t",(M1).upper())
    opciones()


#Bloque Principal
Menu()
