class Autor:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Autor: {self.nome}"


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}, {self.autor}")


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)

    def remover_livro(self, titulo):
        self.livros = [livro for livro in self.livros if livro.titulo != titulo]

    def exibir_livros(self):
        print("Livros na biblioteca:")
        for livro in self.livros:
            livro.exibir_informacoes()


autor1 = Autor("Robert Greene")
autor2 = Autor("Adam Smith")

biblioteca = Biblioteca()
biblioteca.adicionar_livro("As 48 Leis do Poder", autor1)
biblioteca.adicionar_livro("A Riqueza das Nações", autor2)

biblioteca.exibir_livros()
