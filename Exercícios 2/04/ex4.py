class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def andar(self, distancia_km):
        combustivel_necessario = distancia_km / self.consumo_km_por_litro
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro andou {distancia_km} km.")
        else:
            distancia_possivel = self.nivel_combustivel * self.consumo_km_por_litro
            self.nivel_combustivel = 0
            print(f"O combustível acabou após andar {distancia_possivel:.2f} km.")

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, litros):
        self.nivel_combustivel += litros
        print(
            f"Abastecido com {litros} litros de combustível. Nível atual: {self.nivel_combustivel} litros."
        )


meu_fusca = Carro(15)
meu_fusca.adicionar_gasolina(20)
meu_fusca.andar(100)
combustivel_restante = meu_fusca.obter_gasolina()
print(f"Combustível restante: {combustivel_restante:.2f} litros.")
