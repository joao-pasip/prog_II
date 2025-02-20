class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir_extrato(self):
        if not self.transacoes:
            print("Nenhuma transação realizada.")
        else:
            print("Extrato:")
            for transacao in self.transacoes:
                print(transacao)


class Conta:
    _total_contas = 0

    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo
        self.historico = Historico()
        Conta._total_contas += 1

    @classmethod
    def total_contas(cls):
        return cls._total_contas

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.adicionar_transacao(
                f"""Transferência: -R${valor:.2f}
                para {conta_destino.cliente.nome}"""
            )
            conta_destino.historico.adicionar_transacao(
                f"Transferência: +R${valor:.2f} de {self.cliente.nome}"
            )
            print(
                f"""
                Transferência de R${valor:.2f}
                para {conta_destino.cliente.nome} realizada com sucesso."""
            )
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")

    def exibir_extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        self.historico.exibir_extrato()


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


cliente1 = Cliente("João Silva", "123.456.789-00")
cliente2 = Cliente("Maria Oliveira", "987.654.321-00")

conta1 = Conta(cliente1, 1000)
conta2 = Conta(cliente2, 500)

conta1.depositar(200)
conta1.sacar(100)
conta1.transferir(300, conta2)

conta1.exibir_extrato()
conta2.exibir_extrato()

print(f"Total de contas criadas: {Conta.total_contas()}")
