import random
import os

os.system("clear")
print("\n*** BIENVENIDO AL 3 EN RAYA ***\n\n")
print("Quién empieza a jugar?\n")
print('''Elige:
        M - Máquina 🤖 o
        J - Jugador 🙋 x
        S - No quiero elegir, que se haga un sorteo entre Máquina y Jugador 🤷
        ''')


tablero_vacio = '''   |   |  
---+---+---
   |   |  
---+---+---
   |   |   '''

tablero_lleno = ''' 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9 '''


jugadas_permitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indices = [1, 5, 9, 24, 28, 32, 47, 51, 55]
posiciones_ganadoras = [
        (1, 5, 9), (24, 28, 32), (47, 51, 55), # Filas
        (1, 24, 47), (5, 28, 51), (9, 32, 55), # Columnas
        (1, 28, 55), (9, 28, 47)               # Diagonales
    ]


def rellena_casilla(casilla, quien_juega):
    global tablero_vacio, tablero_lleno
    for i in range(1, 10):
        if casilla == i:
            indice = indices[i-1]
            tablero_vacio = tablero_vacio[:indice] + quien_juega + tablero_vacio[indice+1:]
            tablero_lleno = tablero_lleno[:indice] + " " + tablero_lleno[indice+1:]
            print()
            os.system("clear")
            print("\n\n")
            print(tablero_vacio, "\n")


def ganar(tablero_vacio):
    global posiciones_ganadoras
    for pos in posiciones_ganadoras:
        if tablero_vacio[pos[0]] == tablero_vacio[pos[1]] == tablero_vacio[pos[2]] != " ":
            return True
    return False

        

def eleccion_maquina(jugadas_permitidas, tablero_vacio):
    global posiciones_ganadoras

    # Prioridad 1: Verificar si la máquina puede ganar en la siguiente jugada
    for pos in posiciones_ganadoras:
        if tablero_vacio[pos[0]] == tablero_vacio[pos[1]] == "o" and tablero_vacio[pos[2]] == " ":
            return indices.index(pos[2])+1
        if tablero_vacio[pos[0]] == tablero_vacio[pos[2]] == "o" and tablero_vacio[pos[1]] == " ":
            return indices.index(pos[1])+1
        if tablero_vacio[pos[1]] == tablero_vacio[pos[2]] == "o" and tablero_vacio[pos[0]] == " ":
            return indices.index(pos[0])+1

    # Prioridad 2: Verificar si el jugador puede ganar en la siguiente jugada y bloquearlo
    for pos in posiciones_ganadoras:
        if tablero_vacio[pos[0]] == tablero_vacio[pos[1]] == "x" and tablero_vacio[pos[2]] == " ":
            return indices.index(pos[2])+1
        if tablero_vacio[pos[0]] == tablero_vacio[pos[2]] == "x" and tablero_vacio[pos[1]] == " ":
            return indices.index(pos[1])+1
        if tablero_vacio[pos[1]] == tablero_vacio[pos[2]] == "x" and tablero_vacio[pos[0]] == " ":
            return indices.index(pos[0])+1
        
    # Prioridad 3: Hacer una jugada aleatoria en una casilla libre
    return random.choice(jugadas_permitidas)




while True:
    quien_juega = input("Elección: ").upper()
    if quien_juega == "S":
        jugadores = ["J", "M"]
        quien_juega = random.choice(jugadores)
        break
    elif quien_juega in "JM":
        os.system('clear')
        break
    else:
        print("Opción no válida 👎 inténtalo de nuevo.")



while True:
    if quien_juega == "x":
        quien_juega = "M"
    if quien_juega == "o":
        quien_juega = "J"

    if quien_juega == "J":
        quien_juega = "x"
        print("\n\tEres la 'x'. Dime en qué casilla quieres hacer tu jugada?\n\n\tElige uno de los números que ves en el tablero:\n\n")
        print(tablero_lleno)
       
        while True:
            jugada_jugador = int(input("\n\nCasilla: "))
            os.system('clear')
            
            if jugada_jugador in jugadas_permitidas:
                jugadas_permitidas.remove(jugada_jugador)
                break
            
            else:                
                print("\nJugada no permitida ❌ debes elegir el número correspondiente a una casilla que esté vacía.\n")
                print(tablero_lleno)
                print()
                print(tablero_vacio)
        
        rellena_casilla(jugada_jugador, quien_juega)
        if ganar(tablero_vacio) == True:
            print(f"\n\n!Enhorabuena! Has ganado 🥳\n\n")
            break
        elif len(jugadas_permitidas) == 0:
            print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
            break

    elif quien_juega == "M":
        quien_juega = "o"
        jugada_maquina = eleccion_maquina(jugadas_permitidas, tablero_vacio)
        jugadas_permitidas.remove(jugada_maquina)
        rellena_casilla(jugada_maquina, quien_juega)
        if ganar(tablero_vacio) == True:
            print("\n\nLa máquina ha ganado 🤖 Inténtalo de nuevo!\n\n")
            break
        elif len(jugadas_permitidas) == 0:
            print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
            break
        print("\nLa máquina es la 'o' e hizo su jugada, ahora es tu turno.")
    
