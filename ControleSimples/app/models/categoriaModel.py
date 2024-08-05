class Categoria:
    def __init__(self, id, categoria):
        self.__id = id
        self.__descricao = categoria

    @property
    def id(self):
        return self.__id

    @property
    def categoria(self):
        return self.__descricao

    @id.setter
    def id(self, newid):
        self.__id = newid

    @categoria.setter
    def categoria(self, categoria):
        self.__descricao = categoria
