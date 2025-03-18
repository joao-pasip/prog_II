class Tarefa:
    """
    Classe para representar uma tarefa no sistema.

    Atributos:
        descricao (str): Descrição da tarefa
        responsavel (str): Nome do responsável pela tarefa
        status (str): Status atual da tarefa (inicialmente "Pendente")
    """

    def __init__(self, descricao, responsavel):
        """
        Inicializa uma nova tarefa.

        Args:
            descricao (str): Descrição detalhada da tarefa
            responsavel (str): Nome da pessoa responsável pela tarefa
        """
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = "Pendente"

    def marcar_como_concluida(self):
        """
        Altera o status da tarefa para "Concluída".

        Returns:
            None
        """
        self.status = "Concluída"
