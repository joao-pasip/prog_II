from datetime import date, datetime


class Jogador:
    __slots__ = [
        "_nome",
        "_posicao",
        "_data_nascimento",
        "_nacionalidade",
        "_altura",
        "_peso",
    ]

    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self._nome = nome
        self._posicao = posicao
        self._data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self._nacionalidade = nacionalidade
        self._altura = altura
        self._peso = peso

    def get_nome(self):
        return self._nome

    def get_posicao(self):
        return self._posicao

    def get_data_nascimento(self):
        return self._data_nascimento

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.get_data_nascimento().year
        return idade

    def aposentar(self):
        idade_atual = self.calcular_idade()
        if self.get_posicao().upper() == "DF":
            idade_aposentadoria = 40
        elif self.get_posicao().upper() == "MC":
            idade_aposentadoria = 38
        elif self.get_posicao().upper() == "AT":
            idade_aposentadoria = 35
        else:
            print("Posição do jogador desconhecida para cálculo da aposentadoria!")

        anos_restantes = idade_aposentadoria - idade_atual

        return max(0, anos_restantes)

    def imprimir_dados(self):
        print(f"Nome: {self._nome}")
        print(f"Posição: {self._posicao}")
        print(f"Data de Nascimento: {self._data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Nacionalidade: {self._nacionalidade}")
        print(f"Altura: {self._altura} m")
        print(f"Peso: {self._peso} kg")
        print(f"Idade: {self.calcular_idade()} anos")
        anos_para_aposentar = self.aposentar()
        if isinstance(anos_para_aposentar, int):
            print(f"Tempo para aposentadoria: {anos_para_aposentar} anos")
        else:
            print(anos_para_aposentar)


if __name__ == "__main__":
    jogador = Jogador("Pasip", "AT", "26/05/2000", "Brasileira", 1.74, 92)
    jogador.imprimir_dados()
