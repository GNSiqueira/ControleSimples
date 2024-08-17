class Inventario:
    def __init__(self, idinventario, qtdproduto, idproduto):
        self.__idinventario = idinventario
        self.__qtdproduto = qtdproduto
        self.__idproduto = idproduto

    @property
    def idinventario(self):
        return self.__idinventario    
    
    @idinventario.setter
    def idinventario(self, new_idinventario):
        self.__idinventario = new_idinventario

    @property
    def qtdproduto(self):
        return self.__qtdproduto    
    
    @qtdproduto.setter
    def qtdproduto(self, new_qtdproduto):
        self.__qtdproduto = new_qtdproduto

    @property
    def idproduto(self):
        return self.__idproduto    
    
    @idproduto.setter
    def idproduto(self, new_idproduto):
        self.__idproduto = new_idproduto
