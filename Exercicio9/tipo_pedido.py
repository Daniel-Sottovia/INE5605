

class TipoPedido():
    '''
    O atributo fator_distancia eh um float que representa
    o custo pela distancia percorrida para aquele tipo de pedido.
    '''
    def __init__(self, descricao: str, fator_distancia: float):
        self.__descricao = descricao
        self.__fator_distancia = fator_distancia

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def fator_distancia(self):
        return self.__fator_distancia

    @fator_distancia.setter
    def fator_distancia(self, fator_distancia: float):
        if isinstance(fator_distancia, float):
            self.__fator_distancia = fator_distancia
