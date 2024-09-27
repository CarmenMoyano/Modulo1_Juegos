import random
import os

class TicTacToe:

    def __init__(self): # Método constructor 
        self.tablero_vacio = '''                                       |   |  
                                    ---+---+---
                                       |   |  
                                    ---+---+---
                                       |   |   
'''

        self.tablero_lleno = '''                                     1 | 2 | 3
                                    ---+---+---
                                     4 | 5 | 6
                                    ---+---+---
                                     7 | 8 | 9 
 '''
        
        self.jugadas_permitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista de jugadas permitidas
        self.indices = [37, 41, 45, 132, 136, 140, 227, 231, 235] # Índices correspondientes a las posiciones en el string del tablero
        self.posiciones_ganadoras = [
            (37, 41, 45), (132, 136, 140), (227, 231, 235),  # Filas
            (37, 132, 227), (41, 136, 231), (45, 140, 235),  # Columnas
            (37, 136, 235), (45, 136, 227)]                  # Diagonales
        self.quien_juega = None


    def mensaje_bienvenida(self):
        """Muestra el mensaje de bienvenida y las opciones para elegir quién comienza"""
        os.system("clear")
        print("\n\n\t\t\t\t\t\t*** BIENVENIDO AL 3 EN RAYA ***\n\n")
        print("\t\tQuién empieza a jugar?\n")
        print('''\t\tElige:
                            M - Máquina 🤖 o
                            J - Jugador 🙋 x
                            S - No quiero elegir, que se haga un sorteo entre Máquina y Jugador 🤷
                ''')


    def elegir_quien_empieza(self):
        """Permite al usuario elegir quién comienza el juego o seleccionar aleatoriamente"""
        while True:
            self.quien_juega = input("\t\tElección: ").upper()
            if self.quien_juega == "S":
                os.system('clear')
                jugadores = ["J", "M"]
                self.quien_juega = random.choice(jugadores)
                break
            elif self.quien_juega in "JM":
                os.system('clear')
                break
            else:
                print("\n\n\t\t\t\tOpción no válida 👎 inténtalo de nuevo.\n")


    def rellena_casilla(self, casilla, quien_juega):
        """Rellena una casilla del tablero con el símbolo del jugador actual"""
        for i in range(1, 10):
            if casilla == i:
                indice = self.indices[i-1]
                self.tablero_vacio = self.tablero_vacio[:indice] + quien_juega + self.tablero_vacio[indice+1:]
                self.tablero_lleno = self.tablero_lleno[:indice] + " " + self.tablero_lleno[indice+1:]
                print()
                os.system("clear")
                print("\n")
                print(self.tablero_vacio, "\n")


    def ganar(self):
        """Verifica si hay una combinación ganadora en el tablero"""
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] != " ":
                return True
        return False


    def eleccion_maquina(self):
        """Determina la jugada de la máquina con prioridad en ganar o bloquear al jugador"""
        # Prioridad 1: Verificar si la máquina puede ganar en la siguiente jugada
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == "o" and self.tablero_vacio[pos[2]] == " ":
                return self.indices.index(pos[2]) + 1
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[2]] == "o" and self.tablero_vacio[pos[1]] == " ":
                return self.indices.index(pos[1]) + 1
            if self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] == "o" and self.tablero_vacio[pos[0]] == " ":
                return self.indices.index(pos[0]) + 1

        # Prioridad 2: Verificar si el jugador puede ganar en la siguiente jugada y bloquearlo
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == "x" and self.tablero_vacio[pos[2]] == " ":
                return self.indices.index(pos[2]) + 1
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[2]] == "x" and self.tablero_vacio[pos[1]] == " ":
                return self.indices.index(pos[1]) + 1
            if self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] == "x" and self.tablero_vacio[pos[0]] == " ":
                return self.indices.index(pos[0]) + 1

        # Prioridad 3: Hacer una jugada aleatoria en una casilla libre
        return random.choice(self.jugadas_permitidas)


    def jugar(self):
        """Controla el flujo del juego alternando entre el jugador y la máquina"""
        while True:
            if self.quien_juega == "x":
                self.quien_juega = "M"
            if self.quien_juega == "o":
                self.quien_juega = "J"

            if self.quien_juega == "J":
                self.quien_juega = "x"
                print("\n\n\t\tEres la 'x'. Dime en qué casilla quieres hacer tu jugada?\n")
                print("\t\t *** Elige uno de los números que ves en el tablero ***\n\n")
                print(self.tablero_lleno)

                while True:
                    try:
                        jugada_jugador = int(input("\n\n\t\t\tCasilla: "))
                    except ValueError:
                        pass
                    
                    os.system('clear')

                    if jugada_jugador in self.jugadas_permitidas:
                        self.jugadas_permitidas.remove(jugada_jugador)
                        break

                    else:
                        print("\n\tJugada no permitida ❌ debes elegir el número correspondiente a una casilla que esté vacía.\n\n")
                        print(self.tablero_lleno)
                        print()
                        print(self.tablero_vacio)

                self.rellena_casilla(jugada_jugador, self.quien_juega)
                if self.ganar():
                    print(f"\n\n\t\t\t!Enhorabuena! Has ganado 🥳\n\n")
                    break
                elif len(self.jugadas_permitidas) == 0:
                    print(f"\n\n\t\tNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break

            elif self.quien_juega == "M":
                self.quien_juega = "o"
                jugada_maquina = self.eleccion_maquina()
                self.jugadas_permitidas.remove(jugada_maquina)
                self.rellena_casilla(jugada_maquina, self.quien_juega)
                if self.ganar():
                    print("\n\n\t\t\tLa máquina ha ganado 🤖 Inténtalo de nuevo!\n\n")
                    break
                elif len(self.jugadas_permitidas) == 0:
                    print(f"\n\n\t\tNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break
                print("\t\tLa máquina es la 'o' e hizo su jugada, ahora es tu turno.")


# Ejecución principal
if __name__ == "__main__":
    juego = TicTacToe()
    juego.mensaje_bienvenida()
    juego.elegir_quien_empieza()
    juego.jugar()