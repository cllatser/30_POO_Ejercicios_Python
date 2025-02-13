class Operacion:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def suma(self):
        return self.x + self.y

    def multiplicacion(self):
        return self.x * self.y

    def division(self):
        if self.y == 0:
            return f"¡División de {self.x} por {self.y} es imposible!"
        else:
            return self.x / self.y

operacion_01 = Operacion(1, 2)
operacion_02 = Operacion(2, 0)

print(operacion_01.division())
print(operacion_02.division())

print(operacion_01.multiplicacion())
print(operacion_02.multiplicacion())