# from usuario import Convidado
# from casamento import Casamento
# from tarefa import Tarefa
# from presente import Presente


# def menu_interativo():
#     casamento = Casamento("12/12/2025", "Praia de Copacabana")
#     while True:
#         print("\nMenu do App de Casamento")
#         print("1 - Adicionar Convidado")
#         print("2 - Adicionar Tarefa")
#         print("3 - Adicionar Presente")
#         print("4 - Exibir Detalhes do Casamento")
#         print("5 - Listar Presentes")
#         print("6 - Sair")
#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             nome = input("Nome do Convidado: ")
#             email = input("Email do Convidado: ")
#             senha = input("Senha do Convidado: ")
#             convidado = Convidado(nome, email, senha)
#             casamento.adicionar_convidado(convidado)
#             print("Convidado adicionado!")

#         elif opcao == "2":
#             descricao = input("Descrição da Tarefa: ")
#             responsavel = input("Responsável: ")
#             tarefa = Tarefa(descricao, responsavel)
#             casamento.adicionar_tarefa(tarefa)
#             print("Tarefa adicionada!")

#         elif opcao == "3":
#             descricao = input("Descrição do Presente: ")
#             loja = input("Loja: ")
#             preco = input("Preço (R$): ")
#             try:
#                 presente = Presente(descricao, loja, float(preco))
#                 casamento.adicionar_presente(presente)
#                 print("Presente adicionado à lista!")
#             except ValueError:
#                 print("Erro: O preço deve ser um número válido.")

#         elif opcao == "4":
#             print(casamento.exibir_detalhes())

#         elif opcao == "5":
#             print("\nLista de Presentes:")
#             for presente in casamento.listar_presentes():
#                 print(
#                     f"""
#                     - {presente.descricao} (Loja: {presente.loja})
#                     - R$ {presente.preco:.2f}"""
#                 )

#         elif opcao == "6":
#             print("Saindo...")
#             break

#         else:
#             print("Opção inválida! Tente novamente.")


# # Executar menu interativo
# menu_interativo()

from usuario import Convidado
from casamento import Casamento
from tarefa import Tarefa
from presente import Presente


def menu_interativo():
    """
    Interface interativa para gerenciar um casamento.

    Permite adicionar convidados, tarefas e presentes, além de visualizar
    informações do casamento.
    """
    casamento = Casamento("12/12/2025", "Praia de Copacabana")

    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE CASAMENTO ===")
        print("1 - Adicionar Convidado")
        print("2 - Adicionar Tarefa")
        print("3 - Adicionar Presente")
        print("4 - Exibir Detalhes do Casamento")
        print("5 - Listar Presentes")
        print("6 - Listar Convidados")
        print("7 - Listar Tarefas")
        print("8 - Sair")

        try:
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                nome = input("Nome do Convidado: ").strip()
                email = input("Email do Convidado: ").strip()
                senha = input("Senha do Convidado: ").strip()

                if not nome or not email or not senha:
                    print("Erro: Todos os campos são obrigatórios!")
                    continue

                convidado = Convidado(nome, email, senha)
                casamento.adicionar_convidado(convidado)
                print("Convidado adicionado com sucesso!")

            elif opcao == "2":
                descricao = input("Descrição da Tarefa: ").strip()
                responsavel = input("Responsável: ").strip()

                if not descricao or not responsavel:
                    print("Erro: Descrição e responsável são obrigatórios!")
                    continue

                tarefa = Tarefa(descricao, responsavel)
                casamento.adicionar_tarefa(tarefa)
                print("Tarefa adicionada com sucesso!")

            elif opcao == "3":
                descricao = input("Descrição do Presente: ").strip()
                loja = input("Loja: ").strip()
                try:
                    preco = float(input("Preço (R$): ").strip())

                    if preco <= 0:
                        print("Erro: O preço deve ser maior que zero!")
                        continue

                    presente = Presente(descricao, loja, preco)
                    casamento.adicionar_presente(presente)
                    print("Presente adicionado à lista!")

                except ValueError:
                    print("Erro: O preço deve ser um número válido.")

            elif opcao == "4":
                print("\n=== DETALHES DO CASAMENTO ===")
                print(casamento.exibir_detalhes())

            elif opcao == "5":
                print("\n=== LISTA DE PRESENTES ===")
                if not casamento.listar_presentes():
                    print("Nenhum presente cadastrado ainda.")
                else:
                    for presente in casamento.listar_presentes():
                        print(
                            f"""
- {presente.descricao} (Loja: {presente.loja})
  R$ {presente.preco:.2f}"""
                        )

            elif opcao == "6":
                print("\n=== LISTA DE CONVIDADOS ===")
                if not casamento.lista_convidados:
                    print("Nenhum convidado cadastrado ainda.")
                else:
                    for convidado in casamento.lista_convidados:
                        print(f"- {convidado._nome} ({convidado._email})")

            elif opcao == "7":
                print("\n=== LISTA DE TAREFAS ===")
                if not casamento.tarefas:
                    print("Nenhuma tarefa cadastrada ainda.")
                else:
                    for tarefa in casamento.tarefas:
                        print(
                            f"""- {tarefa.descricao}
                            (Responsável: {tarefa.responsavel})"""
                        )

            elif opcao == "8":
                print("\nSaindo do sistema...")
                break

            else:
                print("Opção inválida! Tente novamente.")

        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            continue
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")
            continue


if __name__ == "__main__":
    menu_interativo()
