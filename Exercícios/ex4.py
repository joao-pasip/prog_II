class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99

    def mudar_canal(self, novo_canal):
        if self.canal_min <= novo_canal <= self.canal_max:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}.")
        else:
            print(f"Canal inválido! Insira um número de canal entre {self.canal_min} e {self.canal_max}.")

    def aumentar_volume(self):
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print(f"O volume já está no máximo ({self.volume_max}).")

    def diminuir_volume(self):
        if self.volume > self.volume_min:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print(f"O volume já está no mínimo ({self.volume_min}).")

def main():
    tv = TV()

    while True:
        print(f"\nCanal atual: {tv.canal}, Volume atual: {tv.volume}")
        print("Escolha uma opção:")
        print("1. Mudar canal")
        print("2. Aumentar volume")
        print("3. Diminuir volume")
        print("4. Sair")
        
        opcao = int(input("Opção: "))
        
        if opcao == 1:
            novo_canal = int(input("Digite o novo canal: "))
            tv.mudar_canal(novo_canal)
        elif opcao == 2:
            tv.aumentar_volume()
        elif opcao == 3:
            tv.diminuir_volume()
        elif opcao == 4:
            print("Desligando a TV. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
