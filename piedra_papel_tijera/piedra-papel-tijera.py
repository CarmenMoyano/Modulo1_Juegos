
# Importa la biblioteca random para generar elecciones aleatorias

import random 
import os

class PiedraPapelTijera:
    
    def __init__(self) -> None:
        self.mostrar_reglas()
        
        
    def mostrar_reglas(self):

        os.system("clear")
        print(" Piedra ✊ Papel 🖐️  & Tijera ✌️\n")

        print("- Reglas del Juego Piedra, Papel y Tijera:\n")

        print("     - Dos jugadores eligen una de las tres opciones: Piedra, Papel o Tijera.\n")

        print("- Las reglas para determinar al ganador son:\n")
                
        print("     - Piedra vence a Tijera.\n")

        print("     - Tijera vence a Papel.\n")

        print("     - Papel vence a Piedra.\n")

        print("     - El jugador que gana una ronda obtiene un punto.\n")
                
        print("     - El juego continúa hasta que un jugador haya acumulado 3 puntos, convirtiéndose en el ganador.\n")

    def jugar_partida(self):

        # Inicializa los contadores de partidas ganadas para el jugador y la máquina
        partidas_ganadas_jugador = 0

        partidas_ganadas_maquina = 0

        # Bucle que se ejecuta hasta que el jugador o la máquina ganen 3 partidas

        while partidas_ganadas_jugador < 3 and partidas_ganadas_maquina < 3:

        #El jugador elije su opción
        
            jugador = input("Introduce 1 si quieres ✊, 2 si quieres 🖐️, 3 si quieres ✌️: ")
        
        #Cambiamos el valor de la variable de la elección del jugador (1, 2, 3) a (✊, 🖐️, ✌️)

            if jugador == "1":
                jugador = "✊"

            elif jugador == "2":
                jugador = "🖐️"

            elif jugador == "3":
                jugador = "✌️"

        # Si el jugador no elige una opción válida, muestra un mensaje y vuelve a pedirle la entrada
        
            else:
                print("No has elegido opción correcta ❌❌\n")
        
                continue  # Salta el resto del bucle y vuelve a pedir la entrada del jugador

            #La maquina elige su opción de forma aleatoria

            maquina = ("✊", "🖐️", "✌️")
            maquina = random.choice(maquina)

            #Hacemos las comparativas para ver quien ha ganado

            #Las opciones donde el jugador gana:

            if (maquina == "✊" and jugador == "🖐️") or (maquina == "🖐️" and jugador == "✌️") or (maquina == "✌️" and jugador == "✊"):
                
                partidas_ganadas_jugador = partidas_ganadas_jugador +1 # Incrementa el contador de partidas ganadas del jugador

                print("el 🙋‍♀️ ha sacado", jugador, " y la 🤖", maquina," ha ganado el 🙋‍♀️\n")       
                
                
            #Las opciones donde la máquina gana:
            elif (maquina == "✊" and jugador == "✌️") or (maquina == "🖐️" and jugador == "✊") or (maquina == "✌️" and jugador == "🖐️"):            
            
                partidas_ganadas_maquina += 1  # Incrementa el contador de partidas ganadas de la máquina
                print(f"El 🙋‍♀️ ha sacado {jugador} y la 🤖 {maquina}. Ha ganado la 🤖")
                      
            else:
                
                print(f"El 🙋‍♀️ ha sacado {jugador} y la 🤖 {maquina}. Empate 🤝") # Las opciones donde la máquina y el jugador empatan
            
            print("total ganadas 🙋‍♀️ = ", partidas_ganadas_jugador, " total ganadas 🤖 =", partidas_ganadas_maquina,"\n")
 # Muestra quién ha ganado la serie de 3 partidas

        if partidas_ganadas_maquina > partidas_ganadas_jugador:
            print("Ha ganado la 🤖\n")

        else:
                
            print("Ha ganado el 🙋‍♀️\n")

# Iniciamos la partida
mi_partida = PiedraPapelTijera()

# variable para controlar si se debe volver a jugar
volver_a_jugar = input("¿Quieres empezar a jugar(s) o no(n)?")

os.system("clear")
# Bucle principal que se ejecuta mientras el jugador quiera volver a jugar
while volver_a_jugar == 's':

    mi_partida.jugar_partida()

 
# Pregunta al jugador si quiere volver a jugar
    volver_a_jugar = input("¿Quieres volver a jugar(s) o no(n)?")
    os.system("clear")
# Mensaje de despedida
print("Hasta la próxima 👋👋\n")
