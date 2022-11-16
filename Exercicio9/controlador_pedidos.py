from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    '''
    Busca pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido.
    '''

    def busca_pedido_por_numero(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    '''
    Incluir pedido na lista.
    Tratar os casos de instancias incorretas e pedido duplicado.
    Caso o pedido já exista na lista, gerar a excecao: 
    PedidoDuplicadoException
    '''

    def incluir_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            for linda in self.__pedidos:
                if linda.numero == pedido.numero:
                    raise PedidoDuplicadoException
            self.__pedidos.append(pedido)

    '''
    Exclui pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido excluido
    '''

    def excluir_pedido(self, numero):
        for bonita in self.__pedidos:
            if bonita.numero == numero:
                self.__pedidos.remove(bonita)
                return bonita
        return None

    '''
    Deve calcular o total do faturamento para todos os
    itens pedidos por um CPF. 
    Recebe como parametro:
    distancia: um float que corresponde a distancia percorrida
    cpf: uma string representando o CPF do Cliente a ser faturado
    '''

    def calcular_faturamento_pedidos(self, distancia, cpf):
        pedidos = []
        valor = 0
        for pedido in self.__pedidos:
            if cpf == pedido.cliente.cpf:
                pedidos.append(pedido)
        for pedido in pedidos:
            valor += pedido.calcula_valor_pedido(distancia)
        return valor


if __name__ == '__main__':
    from cliente import Cliente
    from tipo_pedido import TipoPedido
    from item_pedido import ItemPedido
    from cliente_fidelidade import ClienteFidelidade
    daniel = Cliente(cpf='123', nome='Daniel', endereco='Rua Coronel', telefone='9997')
    caio = ClienteFidelidade(cpf='22', nome='Caio', endereco='Avendida Capital', telefone='6799', codigo_fidelidade=22, desconto=0.2)
    urgente = TipoPedido(descricao='pedido urgente', fator_distancia=12)
    tranquilo = TipoPedido(descricao='tranquilo', fator_distancia=5)
    pedido = Pedido(numero=12, cliente=caio, tipo=urgente)
    pedido01 = Pedido(numero=1, cliente=daniel, tipo=urgente)
    pedido02 = Pedido(numero=3, cliente=daniel, tipo=tranquilo)
    pedido.inclui_item_pedido(codigo=444, descricao='bolacha', preco=13.99)
    pedido.inclui_item_pedido(codigo=111, descricao='macarrao', preco=6.00)

    pedido01.inclui_item_pedido(codigo=444, descricao='bolacha', preco=13.99)
    pedido01.inclui_item_pedido(codigo=111, descricao='macarrao', preco=6.00)
    pedido01.mostra_pedidos()

    pedido02.inclui_item_pedido(codigo=171, descricao='chocalate', preco=4.5)
    pedido02.inclui_item_pedido(codigo=323, descricao='anti-tristeza', preco=100)
    pedido02.mostra_pedidos()
    # print(pedido01.calcula_valor_pedido(distancia=6))
    controle = ControladorPedidos()
    controle.incluir_pedido(pedido)
    controle.incluir_pedido(pedido01)
    controle.incluir_pedido(pedido02)
    print(controle.calcular_faturamento_pedidos(distancia=3,cpf='123'))