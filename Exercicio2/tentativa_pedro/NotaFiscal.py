from Cliente import Cliente
from Produto import Produto

class NotaFiscal():
    def __init__(self, cliente: Cliente = None, num_nota: int = None, produtos_vendidos: Produto = None, valor_total: float = None):
        self.__cliente = Cliente
        self.__num_nota = num_nota
        self.__produtos_vendidos = produtos_vendidos

    @property
    def cliente(self):
        return self.__cliente

    @property
    def num_nota(self):
        return self.__num_nota

    @property
    def produtos_vendidos(self):
        return self.__produtos_vendidos

    @property
    def valor_total(self):
        lista = []
        for x in self.__produtos_vendidos:
            valor = x.valor_unit * x.qnt_vendida
            lista.append(valor)
        valor_total = sum(lista)
        return valor_total

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @num_nota.setter
    def num_nota(self, num_nota: int):
        self.__num_nota = num_nota

    @produtos_vendidos.setter
    def produtos_vendidos(self, produtos_vendidos: Produto):
        self.__produtos_vendidos = produtos_vendidos


cliente_1 = Cliente(49526588763, "Pedro", "Florianópolis", "Gmail", "10101010")
produto_1 = Produto(1, "Xbox", 3, 3000.00)
produto_2 = Produto(2, "Playstation", 2, 4500.00)
produto_3 = Produto(3, "PC", 4, 5000.00)
nota_fiscal_1 = NotaFiscal(cliente_1, 1001, [produto_1, produto_2, produto_3])

print(nota_fiscal_1.num_nota)
print(nota_fiscal_1.valor_total)
