class Filme:
    def __init__(self, titulo, duracao_em_minutos):
        self.titulo = titulo
        self.duracao_em_minutos = duracao_em_minutos

    def exibir_duracao_em_horas(self):
        horas = self.duracao_em_minutos // 60
        minutos = self.duracao_em_minutos % 60
        print(
            f"O filme {self.titulo} possui {horas} horas e {minutos} minutos de duração."
        )


filme = Filme("Titanic", 194)
filme.exibir_duracao_em_horas()
