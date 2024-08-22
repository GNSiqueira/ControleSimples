class Movimentacao:
    def __init__(self, id, data, hora, idfuncionario, tipo):
        self.__id = id
        self.__data = data
        self.__hora = hora
        self.__idfuncionario = idfuncionario
        self.__tipo = tipo
    
    @property
    def id(self):
        return self.__id
    
    @property
    def data(self):
        return self.__data
    
    @property
    def hora(self):
        return self.__hora
    
    @property
    def idfuncionario(self):
        return self.__idfuncionario
    
    @property
    def tipo(self):
        return self.__tipo
    
    @id.setter
    def id(self, id):
        self.__id = id

    @data.setter
    def data(self, data):
        self.__data = data

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @idfuncionario.setter
    def idfuncionario(self, idfuncionario):
        self.__idfuncionario = idfuncionario

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo