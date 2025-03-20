class Tarefa:
    """
    Classe para representar uma tarefa no sistema.

    Atributos:
        descricao (str): Descrição da tarefa.
        responsavel (str): Nome do responsável pela tarefa.
        status (str): Status atual da tarefa (inicialmente "Pendente").
    """

    def __init__(self, descricao, responsavel):
        """
        Inicializa uma nova tarefa.

        Args:
            descricao (str): Descrição detalhada da tarefa.
            responsavel (str): Nome da pessoa responsável pela tarefa.
        """
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = "Pendente"  # Status inicial

    def atualizar_status(self, novo_status):
        """
        Atualiza o status da tarefa para um novo valor.

        Args:
            novo_status (str): Novo status da tarefa. Pode ser "Pendente", "Em andamento" ou "Concluída".

        Returns:
            None
        """
        status_validos = ["Pendente", "Em andamento", "Concluída"]

        if novo_status in status_validos:
            self.status = novo_status
            print(
                f"Status da tarefa '{self.descricao}' atualizado para '{novo_status}'."
            )
        else:
            print(
                "Erro: Status inválido. Escolha entre: Pendente, Em andamento ou Concluída."
            )

    def __str__(self):
        """
        Retorna uma representação em string da tarefa.

        Returns:
            str: Representação da tarefa.
        """
        return f"Tarefa: {self.descricao} | Responsável: {self.responsavel} | Status: {self.status}"
