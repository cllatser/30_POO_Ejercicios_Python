class Nota:
    def __init__(self, nota, nombre_estudiante):
        self.nota = nota
        self.nombre_estudiante = nombre_estudiante

    def ha_pasado(self):
        if self.nota >= 75:
            print(f"El estudiante {self.nombre_estudiante} ha pasado")
        else:
            print(f"El estudiante {self.nombre_estudiante} ha reprobado")

nota1 = Nota(75, "Carlos Llatser")
nota1.ha_pasado()
nota1.nota = 68
nota1.ha_pasado()