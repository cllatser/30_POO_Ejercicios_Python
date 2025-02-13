class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        return f"Mi nombre es {self.nombre}, tengo {self.edad} y soy {self.genero}"

    def es_adulto(self):
        if self.edad > 18:
            return True


# persona_01 = Persona("Carlos", 44, "hombre")
# print(persona_01.presentarse())
# print(persona_01.es_adulto())
