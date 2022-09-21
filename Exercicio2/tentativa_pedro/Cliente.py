class Cliente():
    def __init__(self, cpf: int = None, nome: str = None, endereco: str = None, email: str = None, telefone: str = None):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def telefone(self):
        return self.__telefone

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @email.setter
    def email(self, email: str):
        self.__email = email

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
