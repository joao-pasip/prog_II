class Endereco:
    def __init__(self, cep, rua, numero):
        self.cep = cep
        self.rua = rua
        self.numero = numero

    def exibir_endereco(self):
        return f"Endereço: {self.rua}, Número: {self.numero}, CEP: {self.cep}"


class Pessoa:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = None

    def add_endereco(self, cep, rua, numero):
        self.endereco = Endereco(cep, rua, numero)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")
        if self.endereco:
            print(self.endereco.exibir_endereco())
        else:
            print("Endereço não cadastrado.")


if __name__ == "__main__":
    pessoa1 = Pessoa("Pasip", "9999-1234", "123.456.789-00")

    pessoa1.add_endereco("47600-000", "Rua Castro Alves", 274)

    pessoa1.exibir_dados()
