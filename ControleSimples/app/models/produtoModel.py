class Produto: 
    def __init__(self, idproduto, descproduto, valorproduto, idcategoria):
        self.__idproduto = idproduto
        self.__descproduto = descproduto
        self.__valorproduto = valorproduto
        self.__idcategoria = idcategoria

    @property
    def idproduto(self):
        return self.__idproduto

    @property
    def descproduto(self):
        return self.__descproduto

    @property
    def valorproduto(self):
        return self.__valorproduto

    @property
    def idcategoria(self):
        return self.__idcategoria   

    @idproduto.setter
    def idproduto(self, idproduto):
        self.__idproduto = idproduto

    @descproduto.setter
    def descproduto(self, descproduto):
        self.__descproduto = descproduto

    @valorproduto.setter
    def valorproduto(self, valorproduto):
        self.__valorproduto = valorproduto

    @idcategoria.setter
    def idcategoria(self, idcategoria):
        self.__idcategoria = idcategoria