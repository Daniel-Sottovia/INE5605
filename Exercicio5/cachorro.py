from mamifero import Mamifero

class Cachorro(Mamifero):

    def __init__(self):
        super().__init__(volume_som= 3, tamanho_passo= 3)

    def latir(self):
        super(Cachorro, self).produzir_som()
        print('SOM: AU')
        pass

    def mover(self):
        super(Cachorro, self).mover()
        pass


def main():
    dog = Cachorro()
    dog.mover()
    dog.latir()

if __name__ == '__main__':
    main()