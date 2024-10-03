class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= (
                litros_abastecidos  # Atualiza quantidade na bomba
            )
            print(
                f"Você abasteceu {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
            )
            print(
                f"Quantidade de combustível restante na bomba: {self.quantidade_combustivel:.2f} litros."
            )
        else:
            print(
                f"Quantidade de combustível insuficiente. Restam apenas {self.quantidade_combustivel:.2f} litros na bomba."
            )

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros  # Atualiza quantidade na bomba
            print(
                f"Você pagará R${valor_a_pagar:.2f} para abastecer {litros:.2f} litros de {self.tipo_combustivel}."
            )
            print(
                f"Quantidade de combustível restante na bomba: {self.quantidade_combustivel:.2f} litros."
            )
        else:
            print(
                f"Quantidade de combustível insuficiente. Restam apenas {self.quantidade_combustivel:.2f} litros na bomba."
            )

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
        print(f"Valor por litro alterado para R${self.valor_litro:.2f}.")

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        print(f"Tipo de combustível alterado para {self.tipo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(
            f"A quantidade de combustível na bomba foi ajustada para {self.quantidade_combustivel:.2f} litros."
        )


bomba = BombaCombustivel("Gasolina", 6.59, 500)

bomba.abastecer_por_valor(100)
bomba.abastecer_por_litro(20)
bomba.alterar_valor(7.00)
bomba.alterar_combustivel("Etanol")
bomba.alterar_quantidade_combustivel(1000)
