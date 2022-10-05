from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal):

    #@abstractmethod
    def __init__(self,  volume_som: int,tamanho_passo: int):
        super().__init__(tamanho_passo = tamanho_passo)
        self.__volume_som = volume_som

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som: int):
        self.__volume_som = volume_som

    #@abstractmethod
    def mover(self):
        super(Mamifero, self).mover()
        pass

    #@abstractmethod
    def produzir_som(self):
        print(f'MAMIFERO: PRODUZ SOM: {self.__volume_som} ', end='')


def main():
    daniel = Mamifero(4, 5)
    daniel.mover()
    print()
    daniel.produzir_som()

if __name__ == "__main__":
    main()