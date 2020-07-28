import time, random, os
# INICIO DEL JUEGO:
def inicio_Juego():
    print("***BIENVENIDO***")
    time.sleep(1)
    while True:
        ficha = input("Seleccione Ficha: x / o \n>> ")
        ficha = ficha.upper()
        if ficha == "X":
            humano = "X"
            ordenador = "O"
            break
        elif ficha == "O":
            humano = "O"
            ordenador = "X"
            break
        else:
            print('>>PORFAVOR SELECCIONE UNA FICHA POSIBLE<<')
    return humano,ordenador

#CREACION DEL TABLERO:
def tablero():
    print("TRES EN RAYA / TIC-TAC-TOE")
    print()
    print("         |        |       ")
    print(f"1   {matriz[0]}    |2  {matriz[1]}   |3  {matriz[2]}   ")
    print("         |        |       ")
    print('--------------------------')
    print("         |        |       ")
    print(f"4   {matriz[3]}    |5  {matriz[4]}   |6  {matriz[5]}   ")
    print("         |        |       ")
    print('--------------------------')
    print("         |        |       ")
    print(f"7   {matriz[6]}    |8  {matriz[7]}   |9  {matriz[8]}   ")
    print("         |        |       ")

#EMPATE-GANASTE-PERDISTE:
def empate(matriz):
    empate = True
    i=0
    while empate == True and i<9:
        if matriz[1]==" ":
            empate=False
        i = i+1
    return empate

def victoria(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " 
    or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " 
    or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
        return True
    else:
        return False
    
#MOVIMIENTOS:
def mov_Jugador():
    while True:
        posiciones = [0,1,2,3,4,5,6,7,8]
        casilla = int(input('>>Seleccione casilla: '))
        if casilla not in posiciones:
            print('La casilla seleccionada NO se encuentra en el tablero')
        else:
            if matriz[casilla-1] == " ":
               matriz[casilla-1] == humano
               break
            else:
                print('La casilla seleccionada NO se encuentra en el tablero')

def mov_Ord():
    posiciones = [0,1,2,3,4,5,6,7,8]
    casillas = 9
    Stop = False
    
    for i in posiciones:
        copia = List(matriz)
        if copia[i]==" ":
            copia[i]=ordenador
            if victoria(copia)==True:
                casilla=i
    
    if casillas == 9:
        for j in posiciones:
            copia = List(matriz)
            if copia[j]==" ":
                copia[j]=humano
            if victoria(copia)==True:
                casilla= j
    
    if casillas == 9:
        while not Stop:
            casillas = random.randint(0,8)
            if matriz[casillas]== " ":
                Stop = True
    matriz[casilla]=ordenador
        
# DESARROLLO DEL JUEGO:
def JUEGO():
    while True:
        matriz=[" "]*9
        os.system("cls") #limpiara la pantalla al comienzo de cada partida
        humano,ordenador=inicio_Juego()
        partida = True
        ganador = 0
        
        while partida:
            ganador = ganador+1
            os.system("cls")
            tablero()
            if victoria(matriz):
                if ganador%2 == 0:
                    print("**Gana el Jugador**")
                    print("**Fin del Juego**")
                    print("\nReiniciando.....")
                    time.sleep(5)
                    partida=False
                else:
                    print("**Gana el ordenador**")
                    print("**Fin del Juego**")
                    print("\nReiniciando.....")
                    time.sleep(5)
                    partida=False
            elif empate(matriz):
                print("**Gana el Jugador**")
                print("**Fin del Juego**")
                print("\nReiniciando.....")
                time.sleep(5)
                partida=False
            elif ganador%2==0:
                print("El ordenador esta pensando...")
                time.sleep(2)
                mov_Ord()
            else:
                mov_Jugador()
    
# JUEGO()