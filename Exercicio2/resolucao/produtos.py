class Produtos():
    def __init__(self, codigo: int, descricao: str, q_vendida: int, valor_unit: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__quantidade_vendida = q_vendida
        self.__valor_unit = valor_unit

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def quantidade_vendida(self):
        return self.__quantidade_vendida

    @property
    def valor_unit(self):
        return self.__valor_unit

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @quantidade_vendida.setter
    def quantidade_vendida(self, quantidade_vendida: int):
        self.__quantidade_vendida = quantidade_vendida

    @valor_unit.setter
    def valor_unit(self, valor_unit: float):
        self.__valor_unit = valor_unit



