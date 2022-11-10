from mamifero import Mamifero

class Cachorro(Mamifero):

    def __init__(self):
        super().__init__(volume_som= 3, tamanho_passo= 3)

    def latir(self):
        return super().produzir_som() + ' SOM: AU'

    def mover(self):
        return super(Cachorro, self).mover()
