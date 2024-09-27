import random
import os

class Ahorcado:
    def __init__(self):

        self.palabras_ahorcado = [
            "python", "programacion", "desarrollo", "algoritmo", "computadora",
            "tecnologia", "internet", "software", "hardware", "inteligencia",
            "artificial", "robotica", "electronica", "ingenieria", "matematica",
            "estadistica", "física", "quimica", "biologia", "genetica",
            "medicina", "astronomia", "geografia", "historia", "filosofia",
            "literatura", "arte", "musica", "pintura", "escultura",
            "arquitectura", "dibujo", "fotografia", "cine", "teatro",
            "danza", "poesia", "novela", "cuento", "ensayo",
            "periodismo", "redaccion", "publicidad", "marketing", "comunicacion",
            "educacion", "pedagogia", "psicologia", "sociologia", "antropologia"
        ]

        self.dibujo_ahorcado = list('''                                    +---+
                                    |   |
                                        |
                                        |
                                        |
                                        |
                                    =========

    ''')

        self.vidas = 6
        self.letras_falladas = []
        self.palabra = random.choice(self.palabras_ahorcado)
        self.secreto = list("_" * len(self.palabra))

    def empezar_partida (self):
        """Da la bienvenida"""
        os.system("clear")
        print("\t\t\t========================================")
        print("\t\t\t  ¡Bienvenido al emocionante juego del   ")
        print("\t\t\t              AHORCADO!")
        print("\t\t\t========================================")
        print("\n\t\t\tPrepárate para poner a prueba tu ingenio y")
        print("\t\t\t      tus habilidades de adivinanza.")
        print("\n\t\t\t¡Buena suerte, y que comience el juego!\n")
        print("\t\t\t========================================\n\n\n\n")
        print(f"\t\tLa palabra oculta contiene {len(self.palabra)} letras\t {' '.join(self.secreto)}\n\n\n")
        print("".join(self.dibujo_ahorcado)) 
       
    
    def jugar (self):
        """Pide al usuario que elija letra y si esta la descubre"""
               
        self.letra_escogida = input(f"\t\t\tEscoge una letra ")
        if self.letra_escogida in self.palabra:
            for indices, letra in enumerate(self.palabra):    
                if letra == self.letra_escogida:
                    self.secreto[indices] = self.letra_escogida 
                os.system("clear")
                print(f"\t\tFelicidades 🥳\tTu letra está en la palabra oculta  {' '.join(self.secreto)}\n")
                if self.letras_falladas != []: 
                    print(f"\t\tRecuerda que tus letras falladas son: {' , '.join(self.letras_falladas)}\n")                      
                print("".join(self.dibujo_ahorcado))             
            if self.palabra == "".join(self.secreto):
                print(f"\t\tFELICIDADES 🎉🎉 has acertado la palabra {''.join(self.secreto)}, te sobraron {self.vidas} vidas") 
                return
        else:
            self.comprobar_vidas()  
        

    def comprobar_vidas (self):
        """Comprueba el número de vidas y en función de ellas crea el dibujo"""     
        if self.letra_escogida not in self.palabra:
            self.vidas -= 1
            self.letras_falladas.append(self.letra_escogida)
            os.system("clear")        
            print(f"\t\tLo siento 🙃  La palabra oculta no contiene la letra {self.letra_escogida}, las letras falladas son: {' , '.join(self.letras_falladas)} \n\n\t\tSigue intentándolo 😉\t {' '.join(self.secreto)}\n")
            
            if self.vidas == 5:
                self.dibujo_ahorcado[120] = "O"
                print("".join(self.dibujo_ahorcado))

            elif self.vidas == 4:
                self.dibujo_ahorcado[162] = "|"
                print("".join(self.dibujo_ahorcado))           
            elif self.vidas == 3:
                self.dibujo_ahorcado[161] = "/"
                print("".join(self.dibujo_ahorcado))
            elif self.vidas == 2:
                self.dibujo_ahorcado[163] = "\\"
                print("".join(self.dibujo_ahorcado))
            elif self.vidas == 1:
                self.dibujo_ahorcado[203] = "/"
                print("".join(self.dibujo_ahorcado))
            elif self.vidas == 0:  
                self.dibujo_ahorcado[205] = "\\"       
                print("".join(self.dibujo_ahorcado))              
                print(f"\t\tLo siento.🙁  Te has ahorcado ☠.\n\n\t\tLa palabra era {self.palabra}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
if __name__ == "__main__":
    juego = Ahorcado()
    juego.empezar_partida()    
    while juego.vidas > 0:
        juego.jugar()
        
    
