class Funcionario:
    def __init__(self, idfuncionario, nomefuncionario, telFuncionario, loginfuncionario, senhafuncionario):
        self.__idfuncionario = idfuncionario
        self.__telFuncionario = telFuncionario
        self.__nomefuncionario = nomefuncionario
        self.__loginfuncionario = loginfuncionario
        self.__senhafuncionario = senhafuncionario

    @property
    def idfuncionario(self):
        return self.__idfuncionario

    @property
    def telFuncionario(self):
        return self.__telFuncionario

    @property
    def nomefuncionario(self):
        return self.__nomefuncionario

    @property
    def loginfuncionario(self):
        return self.__loginfuncionario

    @property
    def senhafuncionario(self):
        return self.__senhafuncionario
    
    @idfuncionario.setter
    def idfuncionario(self, idfuncionario):
        self.__idfuncionario = idfuncionario

    @telFuncionario.setter
    def telFuncionario(self, telFuncionario):
        self.__telFuncionario = telFuncionario

    @nomefuncionario.setter
    def nomefuncionario(self, nomefuncionario):
        self.__nomefuncionario = nomefuncionario

    @loginfuncionario.setter
    def loginfuncionario(self, loginfuncionario):
        self.__loginfuncionario = loginfuncionario

    @senhafuncionario.setter
    def senhafuncionario(self, senhafuncionario):
        self.__senhafuncionario = senhafuncionario