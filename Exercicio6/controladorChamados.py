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
        # A contagem é na self.__lista_chamadas , não mexer mais
        for chamada in self.__lista_chamadas:
            if chamada.tipo == tipo:
                cont += 1
        return cont

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico,
                       titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        chamada = Chamado(data=data, cliente=cliente, tecnico=tecnico, titulo=titulo
                          ,descricao=descricao, prioridade=prioridade, tipo=tipo)
        '''for ind in self.__lista_chamadas:
            if ind.tipo.codigo == chamada.tipo.codigo:
                return'''
        self.__lista_chamadas.append(chamada)
        return chamada

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        tipo = TipoChamado(codigo=codigo, nome=nome, descricao=descricao)
        for id in self.__lista_tipo_chamadas:
            if id.codigo == codigo:
                return
        self.__lista_tipo_chamadas.append(tipo)
        return tipo

    def tipos_chamados(self):
        cont = 0
        lista = []
        for chamada in self.__lista_chamadas:
            if len(lista) == 0:
                lista.append(chamada.tipo)
                cont += 1
            else:
                if chamada.tipo not in lista:
                    cont += 1
                    lista.append(chamada.tipo)
        return cont

def main():
    caio = Cliente(nome='Caio', codigo=1234)
    arthur = Tecnico(nome='Arthur', codigo= 9876)
    teste = TipoChamado(codigo= 333, descricao='Teste', nome='Teste')
    michel = Cliente(nome='Michel', codigo=5555)
    reclama = TipoChamado(codigo=111, descricao='Reclamacao', nome='Reclamacao')
    daniel = ControladorChamados()
    daniel.inclui_chamado(data = Date(2019,2,20) , cliente= caio,
                          tecnico= arthur, titulo= 'Deus',
                          descricao= 'Domingo', prioridade= 3,
                          tipo= teste)
    print(daniel.total_chamados_por_tipo(tipo= teste))
    daniel.inclui_chamado(data=Date(2021, 7, 9), cliente= michel,
                          tecnico= arthur, titulo= 'Segundo',
                          descricao= 'Sábado', prioridade= 2,
                          tipo= reclama)
    print(daniel.total_chamados_por_tipo(tipo = teste))
    print(daniel.total_chamados_por_tipo(tipo = reclama))
    daniel.inclui_chamado(data = Date(2019,2,20) , cliente= caio,
                          tecnico= arthur, titulo= 'Deus',
                          descricao= 'Domingo', prioridade= 1,
                          tipo= reclama)
    print(daniel.total_chamados_por_tipo(tipo= reclama))


    pass

if __name__ == '__main__':
    main()
