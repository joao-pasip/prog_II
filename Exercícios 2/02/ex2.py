class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print(f"Nome alterado para: {self.nome_correntista}")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")


conta = ContaCorrente(12345, "João Silva")
conta.deposito(1000)
conta.saque(500)
conta.alterar_nome("João Santos")
