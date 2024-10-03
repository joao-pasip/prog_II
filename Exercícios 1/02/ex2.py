class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

def main():
    nome = input("Informe o nome do funcionário: ")
    salario = float(input("Informe o salário do funcionário: "))

    funcionario = Funcionario(nome, salario)

    print(f"\nFuncionário: {funcionario.nome}")
    print(f"Salário atual: R$ {funcionario.salario:.2f}")

    percentual_aumento = float(input("Informe o percentual de aumento: "))
    funcionario.aumentar_salario(percentual_aumento)

    print(f"Salário após aumento: R$ {funcionario.salario:.2f}")

if __name__ == "__main__":
    main()
