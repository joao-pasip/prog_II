class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.historico_consultas = []

    def adicionar_consulta(self, data, descricao):
        consulta = {"data": data, "descricao": descricao}
        self.historico_consultas.append(consulta)
        print(f"Consulta adicionada ao histórico de {self.nome}.")

    def exibir_consultas(self):
        if not self.historico_consultas:
            print(f"{self.nome} não possui consultas registradas.")
        else:
            print(f"Histórico de consultas de {self.nome}:")
            for consulta in self.historico_consultas:
                print(
                    f"""Data: {consulta['data']},
                       Descrição: {consulta['descricao']}"""
                )


if __name__ == "__main__":
    paciente = Paciente("João Silva", 30, "123.456.789-00")
    paciente.adicionar_consulta("2023-10-01", "Consulta de rotina")
    paciente.adicionar_consulta("2023-10-15", "Acompanhamento pós-cirúrgico")
    paciente.exibir_consultas()
