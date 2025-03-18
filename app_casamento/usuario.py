class Usuario:
    """
    Classe base para representar um usuário do sistema.

    Atributos:
        _nome (str): Nome do usuário (encapsulado)
        _email (str): Email do usuário (encapsulado)
        _senha (str): Senha do usuário (encapsulado)
        is_noivo (bool): Indica se o usuário é noivo
    """

    def __init__(self, nome, email, senha, is_noivo=False):
        """
        Inicializa um novo usuário.

        Args:
            nome (str): Nome do usuário
            email (str): Email do usuário
            senha (str): Senha do usuário
            is_noivo (bool): Indica se é noivo (padrão: False)
        """
        self._nome = nome  # Encapsulamento
        self._email = email
        self._senha = senha
        self.is_noivo = is_noivo

    def login(self, email, senha):
        """
        Verifica as credenciais de login do usuário.

        Args:
            email (str): Email para verificação
            senha (str): Senha para verificação

        Returns:
            bool: True se as credenciais estiverem corretas,
            False caso contrário
        """
        return self._email == email and self._senha == senha

    def exibir_dados(self):
        """
        Retorna uma string formatada com os dados do usuário.

        Returns:
            str: String formatada com nome e email
        """
        return f"Nome: {self._nome}, Email: {self._email}"


class Noivo(Usuario):
    """
    Classe derivada de Usuario para representar um noivo.
    Herda todas as funcionalidades da classe Usuario.

    Atributos adicionais:
        lista_convidados (list): Lista de convidados do casamento
        tarefas (list): Lista de tarefas do casamento
    """

    def __init__(self, nome, email, senha):
        """
        Inicializa um novo noivo.

        Args:
            nome (str): Nome do noivo
            email (str): Email do noivo
            senha (str): Senha do noivo
        """
        super().__init__(nome, email, senha)
        self.lista_convidados = []
        self.tarefas = []

    def adicionar_convidado(self, convidado):
        """
        Adiciona um convidado à lista de convidados.

        Args:
            convidado: Informações do convidado a ser adicionado
        """
        self.lista_convidados.append(convidado)

    def adicionar_tarefa(self, tarefa):
        """
        Adiciona uma tarefa à lista de tarefas do casamento.

        Args:
            tarefa: Tarefa a ser adicionada
        """
        self.tarefas.append(tarefa)


class Convidado(Usuario):
    """
    Classe derivada de Usuario para representar um convidado.
    Herda todas as funcionalidades da classe Usuario.

    Atributos adicionais:
        confirma_presenca (bool): Indica se o convidado confirmou presença
    """

    def __init__(self, nome, email, senha):
        """
        Inicializa um novo convidado.

        Args:
            nome (str): Nome do convidado
            email (str): Email do convidado
            senha (str): Senha do convidado
        """
        super().__init__(nome, email, senha)
        self.confirma_presenca = False

    def confirmar_presenca(self):
        """
        Confirma a presença do convidado no evento.
        """
        self.confirma_presenca = True
