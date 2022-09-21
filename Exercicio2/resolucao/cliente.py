class Cliente():
    def __init__(self, cpf: int, nome: str, endereco: str, email: str, telefone: str):
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
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @email.setter
    def email(self, email):
        self.__email = email

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone



