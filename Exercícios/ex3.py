class Aluno:
  def __init__(self, nome, curso, tempo_sem_dormir=0):
    self.nome = nome
    self.curso = curso
    self.tempo_sem_dormir = tempo_sem_dormir

  def estudar(self, qtd_de_horas):
    self.tempo_sem_dormir += qtd_de_horas
    print(f"{self.nome} estudou por {qtd_de_horas} horas.")
    # return self.tempo_sem_dormir
  
  def dormir(self, qtd_de_horas):
    self.tempo_sem_dormir -= qtd_de_horas
    if self.tempo_sem_dormir < 0:
      self.tempo_sem_dormir = 0
      print(f"{self.nome} dormiu por {qtd_de_horas} horas.")
      # return self.tempo_sem_dormir
    else:
      return "Algo não está certo rsrs"
   
  

def main():
  nome_aluno = input('Digite o nome do aluno: ')
  curso = input('Digite o nome do curso: ')

  aluno1 = Aluno(nome_aluno, curso)

  horas_de_estudo = float(input('Quantas horas o aluno estudou? '))
  aluno1.estudar(horas_de_estudo)

  horas_dormidas = float(input("Quantas horas o aluno dormiu? "))
  aluno1.dormir(horas_dormidas)


  print(f"\n{aluno1.nome} está sem dormir há {aluno1.tempo_sem_dormir} horas.")

if __name__ == "__main__":
  main()