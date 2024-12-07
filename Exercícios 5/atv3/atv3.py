from datetime import date, datetime


class Funcionario:
    __slots__ = ["nome", "_salario", "data_admissao"]

    def __init__(self, nome, salario, data_admissao):
        self.nome = nome
        self._salario = salario
        self.data_admissao = datetime.strptime(data_admissao, "%d/%m/%Y").date()

    def get_salario(self):
        return self._salario

    def dar_aumento(self, percentual):
        self._salario += self._salario * (percentual / 100)

    def __str__(self):
        return f"""
        Funcionário: {self.nome}
        Salário: R$ {self.get_salario()}
        Data de admissão: {self.data_admissao.strftime('%d/%m/%Y')}
        """


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        if len(self.funcionarios) < 20:
            self.funcionarios.append(funcionario)
        else:
            print("O departamento já está no limite de 20 funcionários.")

    def remover_funcionario(self, funcionario: Funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
        else:
            print("Funcionário não encontrado no departamento.")

    def dar_aumento_a_todos(self, percentual):
        for funcionario in self.funcionarios:
            funcionario.dar_aumento(percentual)

    def __str__(self):
        return f"Departamento: {self.nome}, Funcionários: {len(self.funcionarios)}"


class Empresa:
    def __init__(self, nome, CNPJ):
        self.nome = nome
        self._CNPJ = CNPJ
        self.departamentos = []

    def get_CNPJ(self):
        return self._CNPJ

    def adicionar_departamento(self, departamento: Departamento):
        if len(self.departamentos) < 10:
            self.departamentos.append(departamento)
        else:
            print("A empresa já possui o limite de 10 departamentos.")

    def transferir_funcionario(
        self,
        funcionario: Funcionario,
        depto_origem: Departamento,
        depto_destino: Departamento,
    ):
        if funcionario in depto_origem.funcionarios:
            depto_origem.remover_funcionario(funcionario)
            depto_destino.adicionar_funcionario(funcionario)
        else:
            print("Funcionário não encontrado no departamento de origem.")

    def __str__(self):
        return f"Empresa: {self.nome}, CNPJ: {self._CNPJ}, Departamentos: {len(self.departamentos)}"


if __name__ == "__main__":
    empresa = Empresa("TechCorp", "12.345.678/0001-90")

    # Criando departamentos
    depto_ti = Departamento("Tecnologia da Informação")
    depto_rh = Departamento("Recursos Humanos")
    empresa.adicionar_departamento(depto_ti)
    empresa.adicionar_departamento(depto_rh)

    # Criando funcionários
    funcionario1 = Funcionario(nome="Ana", salario=5000, data_admissao="01/01/2020")
    funcionario2 = Funcionario(nome="Pasip", salario=6000, data_admissao="15/03/2018")
    funcionario3 = Funcionario(nome="Mariana", salario=5500, data_admissao="10/05/2019")

    # Adicionando funcionários aos departamentos
    depto_ti.adicionar_funcionario(funcionario1)
    depto_ti.adicionar_funcionario(funcionario2)
    depto_rh.adicionar_funcionario(funcionario3)

    # Mostrando informações iniciais
    print(empresa)
    print(depto_ti)
    print(depto_rh)

    # Dando aumento de 10% aos funcionários do departamento de TI
    print("\nDando aumento de 10% aos funcionários do departamento de TI...")
    depto_ti.dar_aumento_a_todos(10)

    # Transferindo um funcionário do departamento de TI para RH
    print("\nTransferindo Ana do departamento de TI para RH...")
    empresa.transferir_funcionario(funcionario1, depto_ti, depto_rh)

    # Mostrando informações finais
    print(depto_ti)
    print(depto_rh)
    for depto in empresa.departamentos:
        for funcionario in depto.funcionarios:
            print(funcionario)
