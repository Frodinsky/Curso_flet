import os
import time
import random
import platform

def reproducir_sonido():
    sonido = "sonido.mp3"  # Asegúrate de que el archivo esté en la misma carpeta
    sistema = platform.system()

    if sistema == "Windows":
        os.system(f'start {sonido}')


def main():
    while True:
        intervalo = random.randint(3, 5)
        time.sleep(intervalo)
        reproducir_sonido()

if __name__ == "__main__":
    main()
