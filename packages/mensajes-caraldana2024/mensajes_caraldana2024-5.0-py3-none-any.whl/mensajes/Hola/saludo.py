import numpy as np

def saludar():
    print("Te saludo desde saludo.saludar")

def prueba():
    print("Esto es una prueba de la nueva versión")

def generar_array(numeros):
    return np.arange(numeros)

class saludo:
    def __init__(self):
        print("Hola, te saludo desde saludo.__init__")


if __name__ == '__main__':
    print(generar_array(5))
