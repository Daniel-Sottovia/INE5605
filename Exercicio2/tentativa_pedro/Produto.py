class Produto():
    def __init__(self, codigo: int = None, descricao: str = None, qnt_vendida: float = None, valor_unit: float = None):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__qnt_vendida = qnt_vendida
        self.__valor_unit = valor_unit

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def qnt_vendida(self):
        return self.__qnt_vendida

    @property
    def valor_unit(self):
        return self.__valor_unit

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @qnt_vendida.setter
    def qnt_vendida(self, qnt_vendida: float):
        self.__qnt_vendida = qnt_vendida

    @valor_unit.setter
    def valor_unit(self, valor_unit: float):
        self.__valor_unit = valor_unit
