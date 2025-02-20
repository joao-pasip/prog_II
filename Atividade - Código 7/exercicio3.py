class Funcionario:
    def __init__(self, nome, data_nascimento, cpf, salario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.salario = salario

    def __str__(self):
        return (
            f"Funcionário: {self.nome}, CPF: {self.cpf}, Salário: R${self.salario:.2f}"
        )


class Despesa:
    def __init__(self, tipo, dia_pagamento, valor):
        self.tipo = tipo
        self.dia_pagamento = dia_pagamento
        self.valor = valor

    def __str__(self):
        return f"Despesa: {self.tipo}, Dia de Pagamento: {self.dia_pagamento}, Valor: R${self.valor:.2f}"


class Empregador:
    def __init__(self):
        self.funcionarios = []
        self.despesas = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} cadastrado com sucesso.")

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
        print(f"Despesa {despesa.tipo} cadastrada com sucesso.")

    def calcular_total_despesas_fixas(self):
        total_salarios = sum(funcionario.salario for funcionario in self.funcionarios)
        total_despesas = sum(despesa.valor for despesa in self.despesas)
        return total_salarios + total_despesas

    def exibir_resumo(self):
        print("\nResumo:")
        print(f"Total de funcionários cadastrados: {len(self.funcionarios)}")
        print(f"Total de despesas cadastradas: {len(self.despesas)}")
        print(
            f"Valor total das despesas fixas do mês: R${self.calcular_total_despesas_fixas():.2f}"
        )


if __name__ == "__main__":
    empresa = Empregador()

    funcionario1 = Funcionario("João Pasip", "2000-05-26", "123.456.789-00", 3000.00)
    funcionario2 = Funcionario(
        "Maria Oliveira", "1985-05-15", "987.654.321-00", 4000.00
    )
    empresa.adicionar_funcionario(funcionario1)
    empresa.adicionar_funcionario(funcionario2)

    despesa1 = Despesa("Aluguel", 5, 2000.00)
    despesa2 = Despesa("Energia", 10, 500.00)
    empresa.adicionar_despesa(despesa1)
    empresa.adicionar_despesa(despesa2)

    empresa.exibir_resumo()
