class Elevador:
    __slots__ = ["_andar_atual", "_total_andares", "_capacidade", "_pessoas_presentes"]

    def __init__(self, total_andares, capacidade):
        self._andar_atual = 0
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._pessoas_presentes = 0

    def get_andar_atual(self):
        return self._andar_atual

    def get_total_andares(self):
        return self._total_andares

    def get_capacidade(self):
        return self._capacidade

    def get_pessoas_presentes(self):
        return self._pessoas_presentes

    def entrar(self):
        if self._pessoas_presentes < self._capacidade:
            self._pessoas_presentes += 1
        else:
            print("O elevador está cheio!")

    def sair(self):
        if self._pessoas_presentes > 0:
            self._pessoas_presentes -= 1
        else:
            print("O elevador está vazio!")

    def subir(self):
        if self._andar_atual < self._total_andares:
            self._andar_atual += 1
        else:
            print("Já está no último andar!")

    def descer(self):
        if self._andar_atual > 0:
            self._andar_atual -= 1
        else:
            print("Já está no térreo!")


if __name__ == "__main__":
    elevador = Elevador(10, 5)

    print(f"Capacidade do elevador: {elevador.get_capacidade()}")
    print(f"Total de andares: {elevador.get_total_andares()}")

    elevador.entrar()
    elevador.entrar()
    print(f"Pessoas no elevador: {elevador.get_pessoas_presentes()}")

    elevador.subir()
    elevador.subir()
    print(f"Andar atual: {elevador.get_andar_atual()}")

    elevador.sair()
    print(f"Pessoas no elevador: {elevador.get_pessoas_presentes()}")

    elevador.descer()
    print(f"Andar atual: {elevador.get_andar_atual()}")
