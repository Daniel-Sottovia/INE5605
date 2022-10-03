from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__lista_chamadas = []
        self.__lista_tipo_chamadas = []

    def total_chamados_por_tipo(self, tipo: TipoChamado):
        cont = 0
        for chamada in self.__lista_tipo_chamadas:
            if chamada == tipo:
                cont += 1

        return cont

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        chamada = Chamado(data=data, cliente=cliente, tecnico=tecnico, titulo=titulo
                          ,descricao=descricao, prioridade=prioridade, tipo=tipo)
        for ind in self.__lista_chamadas:
            if ind.tipo.codigo == chamada.tipo.codigo:
                return
        self.__lista_chamadas.append(chamada)

        return chamada

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        tipo = TipoChamado(codigo=codigo, nome=nome, descricao=descricao)
        for id in self.__lista_chamadas:
            if id.tipo.codigo == tipo.codigo:
                return
        self.__lista_tipo_chamadas.append(tipo)

        return tipo

    def tipos_chamados(self):
        final = defaultdict(int)
        for id in self.__lista_chamadas:
            final[id.tipo] += 1
        return final
