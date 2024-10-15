class Atleta:
    def __init__(self, nome, idade, posicao):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Posição: {self.posicao}"


class Time:
    def __init__(self, nome_time, nome_tecnico):
        self.nome_time = nome_time
        self.nome_tecnico = nome_tecnico
        self.elenco = []

    def add_atleta(self, atleta):
        self.elenco.append(atleta)
        print(f"O atleta {atleta.nome} foi contratado pelo time {self.nome_time}.")

    def remove_atleta(self, atleta):
        if atleta in self.elenco:
            self.elenco.remove(atleta)
            print(f"O atleta {atleta.nome} saiu do time {self.nome_time}.")
        else:
            print(f"O atleta {atleta.nome} não está no time {self.nome_time}.")

    def exibir_elenco(self):
        print(f"Time: {self.nome_time}")
        print(f"Técnico: {self.nome_tecnico}")
        if self.elenco:
            print("Elenco:")
            for idx, atleta in enumerate(self.elenco, 1):
                print(f"{idx}. {atleta}")
        else:
            print("Nenhum atleta no elenco atualmente.")


if __name__ == "__main__":
    atleta1 = Atleta("João", 24, "Atacante")
    atleta2 = Atleta("Pedro", 27, "Zagueiro")
    atleta3 = Atleta("Carlos", 22, "Meio-campo")

    time = Time("FC Pasip", "Técnico Piauhy")

    time.add_atleta(atleta1)
    time.add_atleta(atleta2)

    time.exibir_elenco()

    time.remove_atleta(atleta2)

    time.exibir_elenco()

    time.add_atleta(atleta3)

    time.exibir_elenco()
