from mamifero import Mamifero

class Gato(Mamifero):

    def __init__(self):
        super().__init__(volume_som= 2, tamanho_passo= 2)

    def mover(self):
        super(Gato, self).mover()
        pass

    def miar(self):
        super(Gato, self).produzir_som()
        print('SOM: MIAU')
        pass