import math

class CalculoNumerico:
    def __init__(self, numero):
        self.numero = numero

    def calculo_factorial(self):
        factorial = math.factorial(self.numero)
        print(f"El factorial de {self.numero} es: {factorial}")

    def lista_divisores(self):
        divisores = [i for i in range(1, self.numero + 1) if self.numero % i == 0]
        print(f"La lista de divisores del numero {self.numero} es: {divisores}")

    def es_primo(self):
        if self.numero <= 1:
            print(f"El número no es primo")
        if self.numero == 2:
            print(f"El número es primo")
        if self.numero % 2 == 0:
            print(f"El número no es primo")
        for i in range(3, int(math.sqrt(self.numero))+1, 2):
            if self.numero % i == 0:
                print(f"El número no es primo")
        print(f"El número es primo")


primer_calculo = CalculoNumerico(999)
primer_calculo.calculo_factorial()
primer_calculo.lista_divisores()
primer_calculo.es_primo()
