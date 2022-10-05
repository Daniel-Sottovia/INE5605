from animal import Animal

class Ave(Animal):

    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo=tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        self.__altura_voo = altura_voo

    def mover(self):
        super(Ave, self).mover()
        print('VOANDO')
        pass

    def produzir_som(self):
        print(f'AVE: PRODUZ SOM: ')
        pass