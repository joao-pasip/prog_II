class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []  # Agregação: cliente pode ter várias contas

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito de R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque de R$ {valor:.2f}")
            return True
        return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.append(
                f"Transferência de R$ {valor:.2f} para conta {destino.numero}"
            )
            return True
        return False

    def ver_extrato(self):
        print(f"Extrato da conta {self.numero}:")
        for operacao in self.historico:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)

    def depositar(self, valor):
        taxa = valor * 0.03  # Taxa de serviço de 3%
        return super().depositar(valor - taxa)

    def sacar(self, valor):
        desconto = valor * 0.01  # Desconto de 1% em cada saque
        return super().sacar(valor + desconto)


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)

    def depositar(self, valor):
        rendimento = valor * 0.0015  # Rendimento de 0,15%
        return super().depositar(valor + rendimento)


def somar_saldos(contas):
    total = sum(conta.saldo for conta in contas)
    return total


# Exemplo de uso
cliente1 = Cliente("João Silva", "123.456.789-00")
conta_corrente = ContaCorrente("1001", cliente1, 1000)
conta_poupanca = ContaPoupanca("2001", cliente1, 500)
cliente1.adicionar_conta(conta_corrente)
cliente1.adicionar_conta(conta_poupanca)

conta_corrente.depositar(1000)  # Aplicando taxa de 3%
conta_poupanca.depositar(1000)  # Aplicando rendimento de 0,15%
conta_corrente.sacar(500)  # Aplicando desconto de 1%

conta_corrente.ver_extrato()
conta_poupanca.ver_extrato()

print(f"Saldo total das contas: R$ {somar_saldos(cliente1.contas):.2f}")
