class Circulo:
    def __init__(self, x, y , R):
        self.x = x
        self.y = y
        self.R = R

    def area(self):
        return self.R * self.x * self.y

    def perimetro(self):
        return self.R * self.x + self.y * self.y

    def mostrar_propiedades(self):
        print(f"El circulo tiene un radio de {self.R} y su centro es O{self.x,self.y}\n"
              f"El perímetro del circulo es: {self.perimetro()}\n"
              f"El area del circulo es: {self.area()}\n")

circulo = Circulo(4, 5, 1)
circulo.mostrar_propiedades()