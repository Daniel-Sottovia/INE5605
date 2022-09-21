from cliente import Cliente
from produtos import Produtos

class Nota_fiscal():
    def __init__(self, cliente: Cliente, num_nota: int, vendedor: int, produtos_vendidos: Produtos):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__num_nota = num_nota
        self.__vendedor = vendedor
        self.__produtos_vendidos = []
        if isinstance(produtos_vendidos, Produtos):
            self.__produtos_vendidos.append(produtos_vendidos)
        self.__valor_total = self.valor_total()

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor: int):
        self.__vendedor = vendedor

    @property
    def num_nota(self):
        return self.__num_nota

    def mostrar_produtos_vendidos(self):
        for produtos in self.__produtos_vendidos:
            print(produtos.descricao)

    def adicionar_produto(self, novo_produto: Produtos):
        if isinstance(novo_produto, Produtos):
            self.__produtos_vendidos.append(novo_produto)
            self.__valor_total = self.valor_total()

    def valor_total(self):
        valor = 0
        for produtos in self.__produtos_vendidos:
            valor += produtos.valor_unit * produtos.quantidade_vendida
        return valor

    def get_valor_total(self):
        return self.__valor_total

def main():
    chocolate = Produtos(222, 'chocolate', 3, 4.25)
    leite = Produtos(111, 'leite', 4, 3)

    daniel = Cliente(495, 'Daniel', 'Floripa', 'daniel@gmail.com', '6799999')

    nota01 = Nota_fiscal(cliente= daniel, num_nota=67, vendedor=7, produtos_vendidos=chocolate)
    print(nota01.get_valor_total())
    nota01.adicionar_produto(leite)
    nota01.mostrar_produtos_vendidos()
    print(nota01.get_valor_total())

if __name__ == '__main__':
    main()