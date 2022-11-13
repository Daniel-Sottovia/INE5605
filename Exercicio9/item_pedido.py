
class ItemPedido():

    def __init__(self, codigo :int, descricao :str, preco_unitario :float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo :int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao :str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario :float):
        if isinstance(preco_unitario, float):
            self.__preco_unitario = preco_unitario
