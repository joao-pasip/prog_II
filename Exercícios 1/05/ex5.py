class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1
        print(f"{self.nome} envelheceu {anos} anos e agora tem {self.idade} anos.")

    def engordar(self, peso_ganho):
        self.peso += peso_ganho
        print(f"{self.nome} engordou {peso_ganho}kg e agora pesa {self.peso}kg.")

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido
        print(f"{self.nome} emagreceu {peso_perdido}kg e agora pesa {self.peso}kg.")

    def crescer(self, cm):
        self.altura += cm / 100 
        print(f"{self.nome} cresceu {cm} cm e agora tem {self.altura:.2f} metros.")

def main():
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso (kg): "))
    altura = float(input("Informe a altura (em metros): "))

    pessoa = Pessoa(nome, idade, peso, altura)

    while True:
        print("\nEscolha uma ação:")
        print("1. Envelhecer")
        print("2. Engordar")
        print("3. Emagrecer")
        print("4. Crescer")
        print("5. Sair")
        
        opcao = int(input("Opção: "))

        if opcao == 1:
            anos = int(input("Quantos anos deseja envelhecer? "))
            pessoa.envelhecer(anos)
        elif opcao == 2:
            peso_ganho = float(input("Quantos quilos deseja engordar? "))
            pessoa.engordar(peso_ganho)
        elif opcao == 3:
            peso_perdido = float(input("Quantos quilos deseja emagrecer? "))
            pessoa.emagrecer(peso_perdido)
        elif opcao == 4:
            cm_crescidos = float(input("Quantos centímetros deseja crescer? "))
            pessoa.crescer(cm_crescidos)
        elif opcao == 5:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
