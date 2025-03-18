class Presente:
    """
    Classe para representar um presente no sistema.

    Atributos:
        descricao (str): Descrição detalhada do presente
        loja (str): Nome da loja onde foi comprado
        preco (float): Valor do presente em reais
    """

    def __init__(self, descricao, loja, preco):
        """
        Inicializa um novo presente.

        Args:
            descricao (str): Descrição do presente
            loja (str): Nome da loja onde foi adquirido
            preco (float): Preço do presente em reais

        Note:
            O preço é automaticamente
            convertido para float para garantir operações
            numéricas consistentes
        """
        self.descricao = descricao
        self.loja = loja
        self.preco = float(preco)
