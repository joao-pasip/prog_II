class Triangulo:
    def __init__(self, lado_A, lado_B, lado_C):
        self.lado_A = lado_A
        self.lado_B = lado_B
        self.lado_C = lado_C

    def calcular_perimetro(self):
        return self.lado_A + self.lado_B + self.lado_C

    def get_maior_lado(self):
        return max(self.lado_A, self.lado_B, self.lado_C)

    def eh_triangulo(self):
        return (self.lado_A + self.lado_B > self.lado_C and
                self.lado_A + self.lado_C > self.lado_B and
                self.lado_B + self.lado_C > self.lado_A)

def main():
    lado_A = float(input("Informe o comprimento do lado A: "))
    lado_B = float(input("Informe o comprimento do lado B: "))
    lado_C = float(input("Informe o comprimento do lado C: "))

    triangulo = Triangulo(lado_A, lado_B, lado_C)
    
    if triangulo.eh_triangulo():
        perimetro = triangulo.calcular_perimetro()
        maior_lado = triangulo.get_maior_lado()

        print(f"O perímetro do triângulo é: {perimetro}")
        print(f"O maior lado do triângulo é: {maior_lado}")
    else:
        print("As medidas informadas não formam um triângulo.")

if __name__ == "__main__":
    main()
