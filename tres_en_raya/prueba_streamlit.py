import streamlit
import random

class TicTacToe:
    def __init__(self):
        self.tablero_vacio = '''   |   |  
        ---+---+---
           |   |  
        ---+---+---
           |   |   '''

        self.tablero_lleno = ''' 1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9 '''

        self.jugadas_permitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.indices = [1, 5, 9, 24, 28, 32, 47, 51, 55]
        self.posiciones_ganadoras = [
            (1, 5, 9), (24, 28, 32), (47, 51, 55),  # Filas
            (1, 24, 47), (5, 28, 51), (9, 32, 55),  # Columnas
            (1, 28, 55), (9, 28, 47)                # Diagonales
        ]
        self.quien_juega = None

    def rellena_casilla(self, casilla, quien_juega):
        for i in range(1, 10):
            if casilla == i:
                indice = self.indices[i-1]
                self.tablero_vacio = self.tablero_vacio[:indice] + quien_juega + self.tablero_vacio[indice+1:]
                self.tablero_lleno = self.tablero_lleno[:indice] + " " + self.tablero_lleno[indice+1:]
                streamlit.write(self.tablero_vacio)

    def ganar(self):
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] != " ":
                return True
        return False

    def eleccion_maquina(self):
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

    def elegir_quien_empieza(self):
        self.quien_juega = streamlit.radio("Quién empieza a jugar?", ("M - Máquina 🤖", "J - Jugador 🙋 x", "S - Sorteo 🤷"))
        if self.quien_juega == "S - Sorteo 🤷":
            self.quien_juega = random.choice(["J - Jugador 🙋 x", "M - Máquina 🤖"])
        if self.quien_juega == "J - Jugador 🙋 x":
            self.quien_juega = "J"
        else:
            self.quien_juega = "M"

    def jugar(self):
        if "jugadas_permitidas" not in streamlit.session_state:
            streamlit.session_state.jugadas_permitidas = self.jugadas_permitidas.copy()
        if "quien_juega" not in streamlit.session_state:
            streamlit.session_state.quien_juega = self.quien_juega

        while True:
            if streamlit.session_state.quien_juega == "J":
                streamlit.session_state.quien_juega = "x"
                streamlit.write("\n\tEres la 'x'. Dime en qué casilla quieres hacer tu jugada?\n\n\tElige uno de los números que ves en el tablero:\n\n")
                streamlit.write(self.tablero_lleno)

                jugada_jugador = streamlit.selectbox("\n\nCasilla: ", streamlit.session_state.jugadas_permitidas)
                streamlit.session_state.jugadas_permitidas.remove(jugada_jugador)

                self.rellena_casilla(jugada_jugador, streamlit.session_state.quien_juega)
                if self.ganar():
                    streamlit.success(f"\n\n!Enhorabuena! Has ganado 🥳\n\n")
                    break
                elif len(streamlit.session_state.jugadas_permitidas) == 0:
                    streamlit.info(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break

                streamlit.session_state.quien_juega = "M"

            elif streamlit.session_state.quien_juega == "M":
                streamlit.session_state.quien_juega = "o"
                jugada_maquina = self.eleccion_maquina()
                streamlit.session_state.jugadas_permitidas.remove(jugada_maquina)
                self.rellena_casilla(jugada_maquina, streamlit.session_state.quien_juega)
                if self.ganar():
                    streamlit.warning("\n\nLa máquina ha ganado 🤖 Inténtalo de nuevo!\n\n")
                    break
                elif len(streamlit.session_state.jugadas_permitidas) == 0:
                    streamlit.info(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break
                streamlit.write("\nLa máquina es la 'o' e hizo su jugada, ahora es tu turno.")
                streamlit.session_state.quien_juega = "J"

# Main execution
if __name__ == "__main__":
    streamlit.title("Tic-Tac-Toe")
    juego = TicTacToe()
    juego.elegir_quien_empieza()
    juego.jugar()
