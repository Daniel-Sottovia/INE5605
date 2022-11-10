from mamifero import Mamifero

class Gato(Mamifero):

    def __init__(self):
        super().__init__(volume_som= 2, tamanho_passo= 2)

    def mover(self):
        return super().mover()

    def miar(self):
        return super(Gato, self).produzir_som() + ' SOM: MIAU'
