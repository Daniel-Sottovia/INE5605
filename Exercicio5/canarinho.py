from ave import Ave

class Canarinho(Ave):

    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo=tamanho_passo, altura_voo=altura_voo)

    def cantar(self):
        return super(Canarinho, self).produzir_som() + 'SOM: PIU'

    def mover(self):
        return super().mover()
