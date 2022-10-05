from ave import Ave

class Canarinho(Ave):

    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo=tamanho_passo, altura_voo=altura_voo)

    def produzir_som(self):
        super(Canarinho, self).produzir_som()
        print('PIU')
        pass

    def mover(self):
        super(Canarinho, self).mover()
