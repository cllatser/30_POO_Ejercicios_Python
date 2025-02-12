class Galleta:
    def __init__(self, nombre, forma):
        self.nombre = nombre
        self.forma = forma

    def hornear(self):
        print(f"Esta {self.nombre} ha sido horneada en forma de {self.forma}.\n¡Buen provecho!")


galleta_01 = Galleta("galleta de chocolate", "estrella")
galleta_01.hornear()

