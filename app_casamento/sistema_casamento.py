from usuario import Usuario, Noivo, Convidado
from presente import Presente
from tarefa import Tarefa
from casamento import Casamento


class SistemaCasamento:
    def __init__(self):
        self.usuario_atual = None
        self.casamento = None

    def login(self, email, senha):
        """Realiza o login no sistema"""

        try:
            # Busca o usuário no banco de dados (simulado)
            usuarios = {
                "noivo1@email.com": Noivo("João", "noivo1@email.com", "senha123", True),
                "convidado1@email.com": Usuario(
                    "Maria", "convidado1@email.com", "senha456", False
                ),
            }

            usuario = usuarios.get(email)
            if usuario and usuario.login(email, senha):
                self.usuario_atual = usuario
                return True
            return False
        except Exception as e:
            print(f"Erro no login: {e}")
            return False

    def verificar_permissao_noivo(self):
        """Verifica se o usuário atual é noivo"""
        return self.usuario_atual and isinstance(self.usuario_atual, Noivo)

    def mostrar_menu(self):
        """Exibe o menu baseado no estado de login e no tipo de usuário"""
        if not self.usuario_atual:
            # Exibe opções de login caso o usuário não tenha feito login
            print("Escolha uma opção:")
            print("1. Fazer login")
            print("2. Sair")
        else:
            # Se o usuário estiver logado, exibe o menu adequado
            print(f"Bem-vindo, {self.usuario_atual._nome}!")
            if self.verificar_permissao_noivo():
                # Se o usuário for um noivo, ele tem as seguintes opções
                print("Escolha uma opção:")
                print("1. Criar casamento")
                print("2. Adicionar convidado")
                print("3. Adicionar tarefa")
                print("4. Adicionar presente")
                print("5. Listar convidados")
                print("6. Listar tarefas")
                print("7. Listar presentes")
                print("8. Alterar status de uma tarefa")
                print("9. Sair")
            else:
                # Se o usuário for um convidado, ele tem menos opções
                print("Escolha uma opção:")
                print("1. Listar presentes")
                print("2. Sair")

    def sair(self):
        """Finaliza o sistema"""
        print("Saindo...")
        exit()

    def executar_opcao(self, opcao):
        """Executa a ação escolhida no menu"""
        try:
            if not self.usuario_atual:
                # Se o usuário não estiver logado, oferece o login
                if opcao == "1":
                    email = input("Email: ")
                    senha = input("Senha: ")
                    if self.login(email, senha):
                        print("Login realizado com sucesso!")
                    else:
                        print("Login falhou. Tente novamente.")
                elif opcao == "2":
                    self.sair()
            else:
                if self.verificar_permissao_noivo():
                    # Noivo tem várias opções
                    if opcao == "1":
                        data = input("Data do casamento (DD/MM/AAAA): ")
                        local = input("Local do casamento: ")
                        self.criar_casamento(data, local)
                    elif opcao == "2":
                        nome_convidado = input("Nome do convidado: ")
                        email_convidado = input("Email do convidado: ")
                        senha_convidado = input("Senha do convidado: ")
                        convidado = Convidado(
                            nome_convidado, email_convidado, senha_convidado
                        )
                        self.adicionar_convidado(convidado)
                    elif opcao == "3":
                        descricao_tarefa = input("Descrição da tarefa: ")
                        responsavel = input("Responsável pela tarefa: ")
                        tarefa = Tarefa(descricao_tarefa, responsavel)
                        self.adicionar_tarefa(tarefa)
                    elif opcao == "4":
                        descricao_presente = input("Descrição do presente: ")
                        loja = input("Loja onde foi comprado: ")
                        preco = input("Preço do presente: ")
                        presente = Presente(descricao_presente, loja, preco)
                        self.adicionar_presente(presente)
                    elif opcao == "5":
                        for convidado in self.casamento.lista_convidados:
                            print(convidado.exibir_dados())
                    elif opcao == "6":
                        for i, tarefa in enumerate(self.casamento.tarefas):
                            print(f"{i + 1}. {tarefa.descricao} - {tarefa.status}")
                    elif opcao == "7":
                        for presente in self.casamento.lista_presentes:
                            print(
                                f"{presente.descricao} - {presente.loja} - R${presente.preco}"
                            )
                    elif opcao == "8":
                        self.alterar_status_tarefa()
                    elif opcao == "9":
                        self.sair()
                else:
                    if opcao == "1":
                        for presente in self.casamento.lista_presentes:
                            print(
                                f"{presente.descricao} - {presente.loja} - R${presente.preco}"
                            )
                    elif opcao == "2":
                        self.sair()
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário. Encerrando programa...")
            exit(0)

    def criar_casamento(self, data, local):
        """Cria um casamento no sistema (apenas para noivos)"""
        if not self.verificar_permissao_noivo():
            raise ValueError("Apenas noivos podem criar um casamento.")

        self.casamento = Casamento(data, local)
        print(f"Casamento criado para o dia {data} no local {local}")

    def adicionar_convidado(self, convidado):
        """Adiciona um convidado ao casamento (somente para noivos)"""
        if not self.verificar_permissao_noivo():
            raise ValueError("Apenas noivos podem adicionar convidados")
        self.casamento.adicionar_convidado(convidado)

    def adicionar_tarefa(self, tarefa):
        """Adiciona uma tarefa ao casamento (somente para noivos)"""
        if not self.verificar_permissao_noivo():
            raise ValueError("Apenas noivos podem adicionar tarefas")
        self.casamento.adicionar_tarefa(tarefa)

    def adicionar_presente(self, presente):
        """Adiciona um presente ao casamento (somente para noivos)"""
        if not self.verificar_permissao_noivo():
            raise ValueError("Apenas noivos podem adicionar presentes")
        self.casamento.adicionar_presente(presente)
