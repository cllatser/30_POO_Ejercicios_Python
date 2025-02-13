import random


class Dado:
    def __init__(self, valor:int = 0):
        self.valor = valor

    """
    Método para lanzar el dado y tiene que salir un número entre 1 y 6
    """
    def lanzar_dado(self):
        self.valor = random.randrange(1,6)

    def mostrar_puntos(self):
        print(f"El número de puntos obtenidos es: {self.valor}")


lanzamiento_01 = Dado()
lanzamiento_01.lanzar_dado()
lanzamiento_01.mostrar_puntos()

lanzamiento_01.lanzar_dado()
lanzamiento_01.mostrar_puntos()


