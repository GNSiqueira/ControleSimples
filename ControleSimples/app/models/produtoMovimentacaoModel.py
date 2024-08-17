class ProdutoMovimentacao:
    def __init__(self, idmovimentacao, idproduto, qtd, valor):
        self.__idmovimentacao = idmovimentacao
        self.__idproduto = idproduto
        self.__qtd = qtd
        self.__valor = valor 

    @property
    def idmovimentacao(self):
        return self.__idmovimentacao

    @property
    def idproduto(self):
        return self.__idproduto

    @property
    def qtd(self):
        return self.__qtd

    @property
    def valor(self):
        return self.__valor

    @idmovimentacao.setter
    def idmovimentacao(self, idmovimentacao):
        self.__idmovimentacao = idmovimentacao

    @idproduto.setter
    def idproduto(self, idproduto):
        self.__idproduto = idproduto

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @valor.setter
    def valor(self, valor):
        self.__valor = valor