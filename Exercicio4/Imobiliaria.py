from Imovel import Imovel

class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        if isinstance(imovel, Imovel):
            if imovel not in self.__imoveis:
                self.__imoveis.append(imovel)

    def excluir_imovel(self, imovel: Imovel):
        if isinstance(imovel, Imovel):
            if imovel in self.__imoveis:
                self.__imoveis.remove(imovel)