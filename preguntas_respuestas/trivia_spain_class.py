import random
import os

from tarea1 import tarea1 as t1
from tarea2 import tarea2 as t2
from tarea3 import tarea3 as t3
from tarea4 import tarea4 as t4
from tarea5 import tarea5 as t5

class Trivia:

    def __init__(self):
        self.preguntas_respuestas = None
        self.aciertos = 0
        self.errores = 0
        self.respuesta_correcta = None

    def mensaje_bienvenida(self):
        os.system('clear') 
        print("\n\n\t\t\t\t*** TRIVIA ESPAÑA ***")
        print("----" *20,"\n")
        print("Reglas del juego: Si tiene 3 aciertos ganas y si tienes 3 fallos pierdes.\n\n")
        print("----" *20,"\n")
        print('''Elige un tema:
                            
                            1 - GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA
                            2 - DERECHOS Y DEBERES FUNDAMENTALES
                            3 - ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA
                            4 - CULTURA E HISTORIA DE ESPAÑA
                            5 - SOCIEDAD ESPAÑOLA''')


    def elige_tarea(self):
        while self.preguntas_respuestas == None:
            tarea = input("\n\nINGRESA TU OPCIÓN DEL 1 AL 5 o 'q' para salir: ").lower()
            os.system('clear')
            if tarea == "1":
                self.preguntas_respuestas = t1
                print(f"\nTema elegido: GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA\n")
            elif tarea == "2":
                self.preguntas_respuestas = t2
                print(f"\nTema elegido: DERECHOS Y DEBERES FUNDAMENTALES\n")
            elif tarea == "3":
                self.preguntas_respuestas = t3
                print(f"\nTema elegido: ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA\n")
            elif tarea == "4":
                self.preguntas_respuestas = t4
                print(f"\nTema elegido: CULTURA E HISTORIA DE ESPAÑA\n")
            elif tarea == "5":
                self.preguntas_respuestas = t5
                print(f"\nTema elegido: SOCIEDAD ESPAÑOLA\n")
            elif tarea == "q":
                self.__despedir_juego()
                break 
            else:
                print("\nOpción no valida, vuelve a intentarlo.")
        

    def imprime_pregunta_respuestas(self):
        print("----" *20)
        pregunta = (random.choice(list(self.preguntas_respuestas.keys())))
        print("\n\n",pregunta)
        print("----" *20)
        for clave, valor in self.preguntas_respuestas.items():
            if clave == pregunta:
                self.respuesta_correcta = valor[-1]
                if self.preguntas_respuestas == t2:
                    respuestas = valor[:2]
                else:
                    respuestas = valor[:3]
                for i in respuestas:
                    print(i, end="\t\t")


    def verifica_respuesta_jugador(self):
        while True:    
            while True:
                respuesta_jugador = input("Cuál es la respuesta correcta? ").lower()
                if self.preguntas_respuestas == t2:
                    if respuesta_jugador in "ab":
                        break
                    else:
                        print("\nOpción no válida, intenta otra vez.\n\n")
                else:
                    break
            if respuesta_jugador in "abc":
                if self.respuesta_correcta == respuesta_jugador:
                    self.aciertos += 1
                    print(f"\nMuy bien, la respuesta correcta es {self.respuesta_correcta}. Tienes {self.aciertos} acierto(s).\n\n")
                    break
                else:
                    self.errores += 1
                    print(f"\nLa respuesta correcta es {self.respuesta_correcta}. Tienes {self.errores} fallo(s).\n\n")
                    break
            else:
                print("\nOpción no válida, intenta otra vez.\n\n")


    def ganar_perder(self):
        if self.aciertos == 3:
            print("¡Enhorabuena! Ganaste el juego.\n\n") 
        elif self.errores == 3:
            print("Ooohhhh qué pena, perdiste. ¡No te rindas! Inténtalo de nuevo!\n\n")


    def __despedir_juego(self):
        self.aciertos = self.errores = 4
        print("\nEsperamos verte de nuevo por aquí pronto 😊 ¡Hasta luego! 👋\n\n")
                

    def cambiar_tema(self):
        print("\nIngresa 't' si deseas cambiar de tema: ")


# Ejecución principal
if __name__ == "__main__":
    juego = Trivia()
    juego.mensaje_bienvenida()
    juego.elige_tarea()
    while juego.aciertos < 3 and juego.errores < 3:
        juego.imprime_pregunta_respuestas()
        juego.verifica_respuesta_jugador()
        juego.ganar_perder()