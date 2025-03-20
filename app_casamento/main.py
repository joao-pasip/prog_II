from sistema_casamento import SistemaCasamento
from usuario import Usuario
from tarefa import Tarefa
from presente import Presente

# Inicializa o sistema de casamento
sistema = SistemaCasamento()

# Loop principal
while True:
    try:
        # Exibe o menu de acordo com o estado de login
        sistema.mostrar_menu()

        opcao = input("Escolha uma opção: ")

        # Se o usuário não estiver logado, o menu de login aparece
        if not sistema.usuario_atual:
            if opcao == "1":
                email = input("Email: ")
                senha = input("Senha: ")
                if sistema.login(email, senha):
                    print("Login realizado com sucesso!")
                else:
                    print("Email ou senha incorretos.")
            elif opcao == "2":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        else:
            # Se o usuário estiver logado, o menu adequado será exibido
            if sistema.verificar_permissao_noivo():
                # Menu de noivo
                if opcao == "1":
                    data = input("Data do casamento (DD/MM/AAAA): ")
                    local = input("Local do casamento: ")
                    sistema.criar_casamento(data, local)
                    print("Casamento criado com sucesso!")
                elif opcao == "2":
                    nome = input("Nome do convidado: ")
                    email = input("Email do convidado: ")
                    senha = input("Senha do convidado: ")
                    convidado = Usuario(nome, email, senha, False)
                    sistema.adicionar_convidado(convidado)
                    print(f"Convidado {nome} adicionado com sucesso!")
                elif opcao == "3":
                    descricao_tarefa = input("Descrição da tarefa: ")
                    responsavel = input("Responsável pela tarefa: ")
                    tarefa = Tarefa(descricao_tarefa, responsavel)
                    sistema.adicionar_tarefa(tarefa)
                    print(f"Tarefa {descricao_tarefa} adicionada com sucesso!")
                elif opcao == "4":
                    descricao_presente = input("Descrição do presente: ")
                    loja = input("Loja onde foi comprado: ")
                    preco = input("Preço do presente: ")
                    presente = Presente(descricao_presente, loja, preco)
                    sistema.adicionar_presente(presente)
                    print(f"Presente {descricao_presente} adicionado com sucesso!")
                elif opcao == "5":
                    if sistema.casamento:
                        for convidado in sistema.casamento.lista_convidados:
                            print(convidado.exibir_dados())
                    else:
                        print(
                            "Você precisa criar um casamento antes de adicionar convidados."
                        )
                elif opcao == "6":
                    if sistema.casamento:
                        for tarefa in sistema.casamento.tarefas:
                            print(f"{tarefa.descricao} - {tarefa.status}")
                    else:
                        print(
                            "Você precisa criar um casamento antes de adicionar tarefas."
                        )
                elif opcao == "7":
                    try:
                        if sistema.casamento:
                            for presente in sistema.casamento.lista_presentes:
                                print(
                                    f"{presente.descricao} - {presente.loja} - R${presente.preco}"
                                )
                        else:
                            print(
                                "Você precisa criar um casamento antes de adicionar presentes."
                            )
                    except AttributeError:
                        print(
                            "Erro: Não foi possível acessar a lista de presentes, pois o casamento não foi criado corretamente."
                        )
                elif opcao == "8":
                    if sistema.casamento:
                        print("\nLista de Tarefas:")
                        for i, tarefa in enumerate(sistema.casamento.tarefas):
                            print(f"{i + 1}. {tarefa.descricao} - {tarefa.status}")

                        escolha = (
                            int(
                                input(
                                    "\nEscolha o número da tarefa que deseja atualizar: "
                                )
                            )
                            - 1
                        )

                        if 0 <= escolha < len(sistema.casamento.tarefas):
                            novo_status = input(
                                "Novo status da tarefa (Pendente, Em andamento, Concluída): "
                            )
                            sistema.casamento.tarefas[escolha].status = novo_status
                            print(
                                f"Status da tarefa '{sistema.casamento.tarefas[escolha].descricao}' atualizado para '{novo_status}'."
                            )
                        else:
                            print("Escolha inválida.")
                    else:
                        print(
                            "Você precisa criar um casamento antes de modificar as tarefas."
                        )
                elif opcao == "9":
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                # Menu de convidado
                if opcao == "1":
                    try:
                        if sistema.casamento:
                            for presente in sistema.casamento.lista_presentes:
                                print(
                                    f"{presente.descricao} - {presente.loja} - R${presente.preco}"
                                )
                        else:
                            print("O casamento ainda não foi criado.")
                    except AttributeError:
                        print(
                            "Erro: Não foi possível acessar a lista de presentes, pois o casamento não foi criado corretamente."
                        )
                elif opcao == "2":
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário. Encerrando programa...")
        break  # Sai do loop e encerra o programa
