from ejercicio_06 import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, nivel):
        super().__init__(nombre, edad, genero)
        self.nivel = nivel

    def inscripcion(self, estudiantes_inscritos):
        estudiantes_inscritos.append((self.nombre, self.edad, self.genero, self.nivel))

estudiantes_inscritos = []

estudiante_01 = Estudiante("Carlos", 44, "hombre", "Segundo año")
estudiante_01.inscripcion(estudiantes_inscritos)

estudiante_02 = Estudiante("Lourdes", 46, "mujer", "Segundo año")
estudiante_02.inscripcion(estudiantes_inscritos)

print(estudiantes_inscritos)
