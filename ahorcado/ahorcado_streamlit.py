import random
import streamlit as st

class Ahorcado:
    def __init__(self):
        self.palabras_ahorcado = [
            "python", "programacion", "desarrollo", "algoritmo", "computadora",
            "tecnologia", "internet", "software", "hardware", "inteligencia",
            "artificial", "robotica", "electronica", "ingenieria", "matematica",
            "estadistica", "fisica", "quimica", "biologia", "genetica",
            "medicina", "astronomia", "geografia", "historia", "filosofia",
            "literatura", "arte", "musica", "pintura", "escultura",
            "arquitectura", "dibujo", "fotografia", "cine", "teatro",
            "danza", "poesia", "novela", "cuento", "ensayo",
            "periodismo", "redaccion", "publicidad", "marketing", "comunicacion",
            "educacion", "pedagogia", "psicologia", "sociologia", "antropologia"
        ]
        self.vidas = 6
        self.letras_falladas = []
        self.palabra = random.choice(self.palabras_ahorcado)
        self.secreto = list("_" * len(self.palabra))

    def reset(self):
        self.vidas = 6
        self.letras_falladas = []
        self.palabra = random.choice(self.palabras_ahorcado)
        self.secreto = list("_" * len(self.palabra))

    def jugar(self, letra):
        if letra in self.palabra:
            for indices, l in enumerate(self.palabra):
                if l == letra:
                    self.secreto[indices] = letra
        else:
            self.vidas -= 1
            self.letras_falladas.append(letra)

    def ha_ganado(self):
        return "_" not in self.secreto

    def ha_perdido(self):
        return self.vidas == 0

def main():
    st.title("¡Bienvenido al emocionante juego del AHORCADO!")
    st.write("Prepárate para poner a prueba tu ingenio y tus habilidades de adivinanza.")
    st.write("¡Buena suerte, y que comience el juego!")

    if "juego" not in st.session_state:
        st.session_state.juego = Ahorcado()

    juego = st.session_state.juego

    if st.button("Cambiar de palabra"):
        juego.reset()

    st.write(f"La palabra oculta contiene {len(juego.palabra)} letras")
    st.write(" ".join(juego.secreto))

    try:
        st.image(f"images/ahorcado_{6 - juego.vidas}.gif")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")

    st.write(f"Letras falladas: {', '.join(juego.letras_falladas)}")
    st.write(f"Vidas restantes: {juego.vidas}")

    if juego.ha_ganado():
        st.success(f"¡FELICIDADES! 🎉🎉 has acertado la palabra {''.join(juego.secreto)}. Te sobraron {juego.vidas} vidas.")
    elif juego.ha_perdido():
        st.error(f"Lo siento. 🙁 Te has ahorcado ☠. La palabra era {juego.palabra}")
    else:
        letras = "abcdefghijklmnopqrstuvwxyz"
        cols = st.columns(7)
        for i, letra in enumerate(letras):
            if cols[i % 7].button(letra.upper()):
                juego.jugar(letra)
                break  # Break to update the UI after each guess

if __name__ == "__main__":
    main()
