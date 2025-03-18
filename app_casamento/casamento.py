class Casamento:
    """
    Classe principal para gerenciar um casamento.

    Atributos:
        data (str): Data do casamento
        local (str): Local onde o casamento será realizado
        lista_convidados (list): Lista de convidados confirmados
        tarefas (list): Lista de tarefas pendentes
        lista_presentes (list): Lista de presentes recebidos
    """

    def __init__(self, data, local):
        """
        Inicializa um novo casamento.

        Args:
            data (str): Data do casamento no formato DD/MM/AAAA
            local (str): Nome do local onde será realizado o casamento

        Note:
            As listas de convidados, tarefas e presentes
            são inicializadas vazias e podem ser preenchidas
            posteriormente através dos métodos específicos
        """
        self.data = data
        self.local = local
        self.lista_convidados = []
        self.tarefas = []
        self.lista_presentes = []

    def adicionar_convidado(self, convidado):
        """
        Adiciona um convidado à lista de convidados.

        Args:
            convidado: Objeto do tipo Convidado a ser adicionado

        Returns:
            None
        """
        self.lista_convidados.append(convidado)

    def adicionar_tarefa(self, tarefa):
        """
        Adiciona uma tarefa à lista de tarefas pendentes.

        Args:
            tarefa: Objeto do tipo Tarefa a ser adicionada

        Returns:
            None
        """
        self.tarefas.append(tarefa)

    def adicionar_presente(self, presente):
        """
        Adiciona um presente à lista de presentes recebidos.

        Args:
            presente: Objeto do tipo Presente a ser adicionado

        Returns:
            None
        """
        self.lista_presentes.append(presente)

    def exibir_detalhes(self):
        """
        Retorna uma string com os detalhes básicos do casamento.

        Returns:
            str: Formato "Casamento em [local] na data [data]"
        """
        return f"Casamento em {self.local} na data {self.data}"

    def listar_presentes(self):
        """
        Retorna a lista completa de presentes recebidos.

        Returns:
            list: Lista de objetos do tipo Presente
        """
        return self.lista_presentes
