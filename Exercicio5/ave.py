from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal, ABC):

    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo=tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        self.__altura_voo = altura_voo

    @abstractmethod
    def mover(self):
        return super().mover() + ' VOANDO'

    def produzir_som(self):
        return f'AVE: PRODUZ '
