class Vehiculo:
    def __init__(self, marca, velocidad_inicial:int = 0):
        self.marca = marca
        self.velocidad_inicial = velocidad_inicial

    def acelerar(self, valor):
        self.velocidad_inicial += valor

    def decelerar(self, valor):
        self.velocidad_inicial -= valor

    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es: {self.velocidad_inicial} km/h")


class Coche(Vehiculo):
    def __init__(self, marca, velocidad_inicial:int = 0, bocina:str = "¡tuuut!"):
        super().__init__(marca, velocidad_inicial)
        self.bocina = bocina

    def tocar_claxon(self):
        print(self.bocina)

coche_01 = Coche("Seat", 10)
print(f"La velocidad inicial del coche es: {coche_01.velocidad_inicial}")
coche_01.acelerar(89)
coche_01.mostrar_velocidad()
coche_01.decelerar(36)
coche_01.mostrar_velocidad()
coche_01.tocar_claxon()



