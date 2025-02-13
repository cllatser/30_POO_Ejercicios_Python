class Empleado:
    def __init__(self, nombre, funcion, salario, horas = 0):
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario
        self.horas = horas

    def trabajar(self, numero_horas):
        self.horas += numero_horas
        print(f"El empleado {self.nombre} ha trabajado {self.horas} horas.")

    def info_sueldo(self):
        print(f"El empleado {self.nombre} recibe un salario de {self.salario} euros")

    def dar_aumento(self, aumento):
        self.salario += aumento
        print(f"El empleado {self.nombre} ha recibido una aumento de {aumento} euros, "
              f"lo que le da un salario de {self.salario} euros.")

    def info_funcion(self):
        print(f"El empleado {self.nombre} trabaja como {self.funcion}.")

empleado01 = Empleado("Carlos", "Programador", 3000)
empleado01.trabajar(8)
empleado01.info_sueldo()
empleado01.dar_aumento(900)
empleado01.info_funcion()

