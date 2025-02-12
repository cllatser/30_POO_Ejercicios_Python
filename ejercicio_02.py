class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_informaciones(self):
        print(f"El libro titulado: {self.titulo}, escrito por {self.autor}, se vende a {self.precio} euros.")


libro_01 = Libro("El libro de Enoc", "Nauel", 13.5)
libro_01.mostrar_informaciones()
