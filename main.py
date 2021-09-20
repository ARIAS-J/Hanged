# hanged
import random
import string

from palabras import palabras


def obtener_palabra(palabras):
    # Seleccionar una palabra aleatoria de la lista.
    palabras = random.choice(palabras)

    while "-" in palabras or " "  in palabras:
        palabras = random.choice(palabras)
    return palabras.upper()

def ahorcado():
    print("_________")
    print("|       |")
    print("|       O")
    print("|      /|\ ")
    print("|       |")
    print("|      / \ ")

    print("\n""================================")
    print("Bienvenido al juego del ahorcado")
    print("================================")

    palabra = obtener_palabra(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 5

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Mostrar estado de la palabra.
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(f"Vidas: {vidas}")
        # Mostrar las letras.
        print(f"Palabra: {' '.join(palabra_lista)}")

        usuario = input("Escoge una letra: ").upper()

        # Si la letra seleccionada esta en el abecedario
        # y no se encuentra en el conjunto de letras
        # que ya se han ingresado, se añade al conjunto.
        if usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(usuario)
            # Si la letra esta en la palabras.
            if usuario in letras_por_adivinar:
                letras_por_adivinar.remove(usuario)
                print("")
            else:
                vidas -= 1
                print(f"\nTu letra {usuario} no esta en la palabra.")
        elif usuario in letras_adivinadas:
            print("\nLa letra seleccionada ya ha sido escogida. Escoger una letra nueva.")

        else:
            print("La letra no es valida.")

    if vidas == 0:
        print(f"Te has ahorcado perdiste. La palabra era {palabra}")
    else:
        print(f"Felicidades Adivinaste la Palabra {palabra}")


ahorcado()