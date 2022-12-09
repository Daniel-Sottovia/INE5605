from train import ExemploView

class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__main_view = ExemploView()

    def __new__(cls):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
        return ControladorPrincipal.__instance

    def run(self):
        (botao, dados) = self.__main_view.open()

if __name__ == '__main__':
    daniel = ControladorPrincipal().run()