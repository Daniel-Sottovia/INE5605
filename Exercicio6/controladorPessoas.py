from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str):
        cliente = Cliente(codigo=codigo, nome=nome)
        for ind in self.__clientes:
            if ind.codigo == cliente.codigo:
                return
        self.__clientes.append(cliente)
        return cliente

    def inclui_tecnico(self, codigo: int, nome: str):
        tecnico = Tecnico(codigo= codigo, nome= nome)
        for ind in self.__tecnicos:
            if ind.codigo == tecnico.codigo:
                return
        self.__tecnicos.append(tecnico)
        return tecnico